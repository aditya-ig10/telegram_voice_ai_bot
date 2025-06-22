"""SDK to access the list of models available via the API."""

from typing import Any, Coroutine, Union

from google.protobuf import empty_pb2
from ..proto.v2 import models_pb2, models_pb2_grpc

# TODO(pohlen): Add APIs to mimic other SDKs more closely.


class Models:
    """Accessor for the models API."""

    def __init__(self, client: models_pb2_grpc.ModelsStub):
        """Initializes a new instance of the `Models` class.

        Args:
            client: gRPC client to use.
        """
        self._client = client

    def list_language_models(
        self,
    ) -> Union[
        models_pb2.ListLanguageModelsResponse,
        Coroutine[Any, Any, models_pb2.ListLanguageModelsResponse],
    ]:
        """Lists all language models available via the API.

        Returns:
            List of model configurations.
        """
        return self._client.ListLanguageModels(empty_pb2.Empty())

    def list_embedding_models(
        self,
    ) -> Union[
        models_pb2.ListEmbeddingModelsResponse,
        Coroutine[Any, Any, models_pb2.ListEmbeddingModelsResponse],
    ]:
        """Lists all embedding models available via the API.

        Returns:
            List of model configurations.
        """
        return self._client.ListEmbeddingModels(empty_pb2.Empty())
