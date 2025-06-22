"""Embedder API to embed text data."""

from typing import Tuple, AsyncGenerator
from ..proto import embedder_public_pb2, embedder_public_pb2_grpc


class AsyncEmbedder:
    """AsyncEmbedder is a client to the raw embedding service."""

    def __init__(self, stub: embedder_public_pb2_grpc.EmbedderStub):
        """Initializes a new instance of the `AsyncEmbedder` class.

        Args:
            stub: The gRPC stub to use for interacting with the API.
        """
        self._stub = stub

    async def embed(self, texts: list[str], model_name: str):# -> list[Tuple[list[float], int]]:
        """Embeds the given texts.

        Args:
            texts: The list of raw texts to embed.
            model_name: The name of the model to use for embedding.

        Returns:
            A list of tuples, where each tuple contains the embedding and the shape.
        """

        request = embedder_public_pb2.EmbedRequest(texts=texts, model_name=model_name)
        response = await self._stub.Embed(request)
        for embedding in response.embeddings:
            yield embedding.values, embedding.shape



