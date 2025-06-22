"""Wrappers around the bare gRPC bindings."""

import os
from typing import Optional

import grpc

from . import chat, compat, files, grok, sampler, embedder
from ..proto import (
    chat_pb2_grpc,
    files_pb2_grpc,
    sampler_public_pb2_grpc,
    stateless_chat_pb2_grpc,
    embedder_public_pb2_grpc
)


class Client:
    """Client for connecting to the xAI API.

    The client uses an API key, which is either read from the environment variable `XAI_API_KEY` or
    provided by the `api_key` constructor argument. API keys can be created and managed in our IDE,
    which is available under ide.x.ai (click on your username in the top right hand corner).

    The API is hosted on api.x.ai, and we connect via port 443.
    """

    chat: chat.AsyncChat
    files: files.AsyncFiles
    grok: grok.AsyncGrok
    sampler: sampler.AsyncSampler
    embedder: embedder.AsyncEmbedder

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        initial_rng_seed: Optional[int] = None,
        api_host: str = "api.x.ai",
        metadata: Optional[tuple[tuple[str, str]]] = None,
    ) -> None:
        """Initializes a new instance of the `Client` class.

        Args:
            api_key: API key to use. If unspecified, the API key is read from the `XAI_API_KEY`
                environment variable.
            initial_rng_seed: Used to make calls to the API deterministic given the initial seed and
                the order of API calls. If unspecified, a random seed will be sampled for every new
                instance of the `Client` class.
            api_host: Hostname of the API server.
            metadata: Metadata to be sent with each gRPC request. Each tuple should contain a key/value pair

        Raises:
            ValueError: If the `XAI_API_KEY` environment variable is not set.
            ValueError: If the API key is empty.
        """
        if api_key is None:
            api_key = _get_api_from_env()

        if not api_key:
            raise ValueError("Empty xAI API key provided.")

        # Create a channel to connect to the API host. Use the API key for authentication.
        call_credentials = grpc.metadata_call_credentials(_APIAuthPlugin(api_key, metadata))
        if api_host.startswith("localhost:"):
            channel_credentials = grpc.local_channel_credentials()
        else:
            channel_credentials = grpc.ssl_channel_credentials()
        credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
        async_channel = grpc.aio.secure_channel(api_host, credentials)
        sync_channel = grpc.secure_channel(api_host, credentials)

        # Create the stubs used by the SDK. Note that they don't create any connections until being
        # used.
        self.sampler = sampler.AsyncSampler(
            sampler_public_pb2_grpc.SamplerStub(channel=async_channel), initial_rng_seed
        )
        self.chat = chat.AsyncChat(stateless_chat_pb2_grpc.StatelessChatStub(channel=async_channel))
        self.grok = grok.AsyncGrok(chat_pb2_grpc.ChatStub(channel=async_channel))
        self.files = files.AsyncFiles(files_pb2_grpc.FileStub(channel=async_channel))
        self.embedder = embedder.AsyncEmbedder(embedder_public_pb2_grpc.EmbedderStub(channel=async_channel))

        # OpenAI-compatible client.
        self.compat = compat.Client(sync_channel, async_channel)


def _get_api_from_env() -> str:
    """Reads the API key from the `XAI_API_KEY` environment variable.

    Returns:
        The API key.

    Raises:
        ValueError: If the `XAI_API_KEY` environment variable is not set.
    """
    api_key = os.environ.get("XAI_API_KEY")
    if api_key is None:
        raise ValueError(
            "Trying to read the xAI API key from the XAI_API_KEY environment variable but it doesn't exist."
        )
    else:
        return api_key


class _APIAuthPlugin(grpc.AuthMetadataPlugin):
    """A specification for API-key based authentication."""

    def __init__(self, api_key: str, metadata) -> None:
        """Initializes a new instance of the `_APIAuthPlugin` class.

        Args:
            api_key: A valid xAI API key.
            metadata: Metadata to be sent with each gRPC request. Each tuple should contain a key/value pair
        """
        self._api_key = api_key
        self._metadata = metadata

    def __call__(
        self, context: grpc.AuthMetadataPluginCallback, callback: grpc.AuthMetadataPluginCallback
    ):
        """See `grpc.AuthMetadataPlugin.__call__`."""
        del context  # Unused.

        api_key = ("apikey", self._api_key)
        if self._metadata is not None:
            metadata = self._metadata + (api_key,)
        else:
            metadata = (api_key,)
        callback(metadata, None)
