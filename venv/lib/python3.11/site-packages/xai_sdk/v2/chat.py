"""Exposes a chat API."""

import datetime
from typing import Any, AsyncGenerator, Coroutine, Optional, Generator, Literal, TypedDict, Union

from ..proto.v2 import chat_pb2, chat_pb2_grpc, image_pb2


class ChatCompletionMessageParam(TypedDict, total=False):
    """Describes the structure of a `Message` object."""

    content: Union[str, list[dict]]
    role: Union[Literal["system"], Literal["user"], Literal["assistant"], Literal["function"]]


_UNSUPPORTED_CONTENT_TYPE_ERROR_TEMPLATE = (
    "The '{}' content type is not supported by the xAI API. Please remove it."
)


class Chat:
    """Exposes the Chat APIs."""

    def __init__(self, client: chat_pb2_grpc.ChatStub):
        """Initializes a new instance of the `Chat` class.

        Args:
            client: The gRPC client to use.
        """
        self.completions = Completions(client)


class Completions:
    """Implements a chat completions API."""

    def __init__(self, client: chat_pb2_grpc.ChatStub):
        """Initializes a new instance of the `Completions` class.

        Args:
            client: The gRPC client to use.
        """
        self._client = client

    def create(
        self,
        *,
        messages: list[ChatCompletionMessageParam],
        model: str,
        max_tokens: Optional[int] = None,
        n: Optional[int] = None,
        seed: Optional[int] = None,
        stop: Union[Optional[str], list[str]] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        user: str = "",
        stream: Optional[bool] = None,
        timeout: Optional[datetime.timedelta] = None,
    ) -> Union[
        chat_pb2.GetChatCompletionResponse,
        Generator[chat_pb2.GetChatCompletionChunk, None, None],
        Coroutine[Any, Any, chat_pb2.GetChatCompletionResponse],
        Generator[chat_pb2.GetChatCompletionChunk, None, None],
        AsyncGenerator[chat_pb2.GetChatCompletionChunk, None],
    ]:
        """Creates a new chat completion by calling the API.

        Args:
            messages: List of messages that have been exchanged in the conversation (i.e. the
                message history).
            model: ID of the model to sample from. If empty/not provided, the default model will be
                used.
            max_tokens: Maximum number of tokens to sample from the model.
            n: Number of concurrent completions to generate.
            seed: Random number generator seed to use. Makes sampling deterministic.
            stop: A sequence of stop strings. If any of these strings is observed in the model's
                output, sampling is stopped afterward.
            temperature: Controls the sampling temperature. The smaller the value, the less varied
                answers become.
            top_p: Sampling threshold of the nucleus sampling algorith. Only token within the top-p
                percentile will be considered for sampling.
            user: An opaque string used in the backend to associate the request with. Can be useful
                for detecting abuse.
            stream: If true, the function returns a stream of chunks instead of waiting for the
                entire response to finish before returning.
            timeout: Maximum request time before a Timeout exception is raised.

        Returns:
            Either a completion or a stream of chunks if `stream=True`.
        """
        request = _build_request(
            messages, model, max_tokens, n, seed, stop, temperature, top_p, user
        )

        kwargs = {}
        if timeout is not None:
            kwargs["timeout"] = timeout.total_seconds()

        if stream:
            return self._client.GetCompletionChunk(request, **kwargs)
        else:
            return self._client.GetCompletion(request, **kwargs)


def _build_request(
    messages: list[ChatCompletionMessageParam],
    model: str,
    max_tokens: Optional[int],
    n: Optional[int],
    seed: Optional[int],
    stop: Union[Optional[str], list[str]],
    temperature: Optional[float],
    top_p: Optional[float],
    user: str,
) -> chat_pb2.GetCompletionsRequest:
    """Builds the completions request from"""
    # The gRPC API only supports an array of stop strings. If a single string was provided, wrap
    # it in a list.
    if isinstance(stop, str):
        stop = [stop]

    def _parse_message(message):
        if isinstance(message["content"], str):
            content = [
                chat_pb2.Content(
                    text=message["content"],
                )
            ]
        elif isinstance(message["content"], list):
            content = []
            for content_dict in message["content"]:
                content_type = content_dict["type"]
                if content_type in ("text",):
                    content.append(
                        chat_pb2.Content(
                            text=content_dict["text"],
                        )
                    )
                elif content_type == "image_url":
                    if content_dict["image_url"].get("detail", None) is not None:
                        if content_dict["image_url"]["detail"] == "low":
                            detail = image_pb2.ImageDetail.DETAIL_LOW
                        elif content_dict["image_url"]["detail"] == "high":
                            detail = image_pb2.ImageDetail.DETAIL_HIGH
                        else:
                            detail = image_pb2.ImageDetail.DETAIL_AUTO
                    else:
                        detail = image_pb2.ImageDetail.DETAIL_AUTO

                    content.append(
                        chat_pb2.Content(
                            image_url=image_pb2.ImageUrlContent(
                                image_url=content_dict["image_url"]["url"], detail=detail
                            ),
                        )
                    )
                else:
                    raise ValueError(_UNSUPPORTED_CONTENT_TYPE_ERROR_TEMPLATE.format(content_type))
        else:
            raise ValueError("Content must be either a string or a list of dictionary.")

        return chat_pb2.Message(
            content=content,
            role=_extract_role(message["role"]),
        )

    # Create the request proto.
    return chat_pb2.GetCompletionsRequest(
        messages=map(_parse_message, messages),
        model=model or "",
        max_tokens=max_tokens,
        n=n,
        seed=seed,
        stop=stop,
        temperature=temperature,
        top_p=top_p,
        user=user,
    )


def _extract_detail(detail: Optional[str]) -> image_pb2.ImageDetail:
    """Returns the image detail specified in the string and falls back to "AUTO"."""
    if detail == "low":
        return image_pb2.ImageDetail.DETAIL_LOW
    elif detail == "high":
        return image_pb2.ImageDetail.DETAIL_HIGH
    return image_pb2.ImageDetail.DETAIL_AUTO


def _extract_role(role: Optional[str]) -> chat_pb2.MessageRole:
    """Returns the role indicated in the string."""
    if role == "user":
        return chat_pb2.MessageRole.ROLE_USER
    elif role == "assistant":
        return chat_pb2.MessageRole.ROLE_ASSISTANT
    elif role == "system":
        return chat_pb2.MessageRole.ROLE_SYSTEM
    elif role == "function":
        return chat_pb2.MessageRole.ROLE_FUNCTION

    raise ValueError(f"Unrecognized role `{role}`.")
