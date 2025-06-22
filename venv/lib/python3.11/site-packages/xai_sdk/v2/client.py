"""Wrappers around the bare gRPC bindings."""

import os
from typing import Optional

import grpc

from . import chat, embeddings, models
from ..proto.v2 import (
    chat_pb2_grpc,
    embed_pb2_grpc,
    models_pb2_grpc,
)


class Client:
    """Synchronous client for connecting to the xAI API.

    The client uses an API key, which is either read from the environment variable `XAI_API_KEY` or
    provided by the `api_key` constructor argument. API keys can be created and managed in our API
    console, which is available under console.x.ai.

    The API is hosted on api.x.ai, and we connect via port 443.
    """

    chat: chat.Chat
    embeddings: embeddings.Embedding
    models: models.Models

    def __init__(
        self,
        api_key: Optional[str] = None,
        asynchronous: bool = False,
        *,
        api_host: str = "api.x.ai",
        metadata: Optional[tuple[tuple[str, str]]] = None,
    ) -> None:
        """Initializes a new instance of the `Client` class.

        Args:
            api_key: API key to use. If unspecified, the API key is read from the `XAI_API_KEY`
                environment variable.
            asynchronous: If true, the client is asynchronous and all API calls need to be awaited.
            api_host: Hostname of the API server.
            metadata: Metadata to be sent with each gRPC request. Each tuple should contain a
                key/value pair.

        Raises:
            ValueError: If the `XAI_API_KEY` environment variable is not set.
            ValueError: If the API key is empty.
        """
        if asynchronous:
            channel = grpc.aio.secure_channel(
                api_host, _create_channel_credentials(api_key, api_host, metadata)
            )
        else:
            channel = grpc.secure_channel(
                api_host, _create_channel_credentials(api_key, api_host, metadata)
            )

        self.chat = chat.Chat(chat_pb2_grpc.ChatStub(channel))
        self.embeddings = embeddings.Embedding(embed_pb2_grpc.EmbedderStub(channel))
        self.models = models.Models(models_pb2_grpc.ModelsStub(channel))


def _create_channel_credentials(
    api_key: Optional[str], api_host: str, metadata: Optional[tuple[tuple[str, str]]]
):
    """Creates the credentials for the gRPC channel."""
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
    return grpc.composite_channel_credentials(channel_credentials, call_credentials)


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
            "Trying to read the xAI API key from the XAI_API_KEY environment variable "
            "but it doesn't exist."
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

        api_key = ("authorization", f"Bearer {self._api_key}")
        if self._metadata is not None:
            metadata = self._metadata + (api_key,)
        else:
            metadata = (api_key,)
        callback(metadata, None)
