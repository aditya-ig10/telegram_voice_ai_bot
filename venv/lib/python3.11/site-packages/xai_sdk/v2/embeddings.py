"""Implements the text/image embedding API."""

import datetime
from typing import Any, Coroutine, Literal, Optional, Union
from ..proto.v2 import embed_pb2, embed_pb2_grpc, image_pb2


class Embedding:
    """Exposes the embedding APIs."""

    def __init__(self, client: embed_pb2_grpc.EmbedderStub):
        """Creates a new instance of the `Embedding` class.

        Args:
            client: The gRPC client to use.
        """
        self._client = client

    def create(
        self,
        input: Union[str, image_pb2.ImageUrlContent, list[Union[str, image_pb2.ImageUrlContent]]],
        model: str,
        encoding_format: Optional[Literal["float", "base64"]] = None,
        user: str = "",
        timeout: Optional[datetime.timedelta] = None,
    ) -> Union[embed_pb2.EmbedResponse, Coroutine[Any, Any, embed_pb2.EmbedResponse]]:
        """Creates embedding vectors for the provided inputs.

        Args:
            input: The text/images that shall be embedded. Note that not every model supports both
                modalities. The input can either be a single string, a single `ImageUrl` proto, or
                a list of both. When a list is presented, all inputs are embedded concurrently.
            model: Name of the model to use. You can get a list of all available models via the
                `models` API.
            encoding_format: They way the encoded vectors are encoded. "float" encodes them as an
                array of Python floats and "base64" encodes them as a base64-encoded array of
                32-bit floats, that can be loaded into a numpy array.
            user: An opaque string identifying the client' user of the API. Only used for auditing
                purposes.
            timeout: A request timeout.

        Returns:
            Response of the embedding RPC.
        """
        # Convert the input to the correct proto representation.
        if isinstance(input, str) or isinstance(input, image_pb2.ImageUrlContent):
            input = [_convert_input(input)]
        elif isinstance(input, list):
            input = [_convert_input(i) for i in input]
        else:
            raise ValueError(f"Unrecognized embedding input type: {input}")

        if encoding_format == "base64":
            encoding_format = embed_pb2.EmbedEncodingFormat.FORMAT_BASE64
        else:
            # Default to float encoding.
            encoding_format = embed_pb2.EmbedEncodingFormat.FORMAT_FLOAT

        request = embed_pb2.EmbedRequest(
            input=input, model=model, encoding_format=encoding_format, user=user
        )

        kwargs = {}
        if timeout is not None:
            kwargs["timeout"] = timeout.total_seconds()

        return self._client.Embed(request, **kwargs)


def _convert_input(input: Union[str, image_pb2.ImageUrlContent]) -> embed_pb2.EmbedInput:
    """Converts an input to the API wrapper to the correct proto format."""
    if isinstance(input, str):
        return embed_pb2.EmbedInput(string=input)
    elif isinstance(input, image_pb2.ImageUrlContent):
        return embed_pb2.EmbedInput(image_url=input)
    raise ValueError(f"Unrecognized embedding input type: {input}")
