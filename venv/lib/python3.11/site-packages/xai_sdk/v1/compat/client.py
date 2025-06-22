"""Implements an OpenAI-compatible client object."""

import grpc

from . import chat
from ...proto import compat_chat_pb2_grpc


class Client:
    """An OpenAI-compatible API client."""

    def __init__(self, sync_channel: grpc.Channel, async_channel: grpc.aio.Channel):
        """

        Args:
            sync_channel: Channel to use for synchronous communication.
            async_channel: Channel to use for asynchronous communication.
        """
        del async_channel  # Unused for now.
        self.chat = chat.Chat(compat_chat_pb2_grpc.ChatStub(sync_channel))
