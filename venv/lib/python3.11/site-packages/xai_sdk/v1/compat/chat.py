"""Implementation of an OpenAI-compatible Chat API."""

import dataclasses
import random
from typing import Any, Optional, Generator, Literal, TypedDict, Union

from ...proto import compat_chat_pb2, compat_chat_pb2_grpc


class ResponseFormat(TypedDict, total=False):
    """Describes the structure of the `response_format` object."""

    type: Literal["text", "json_object"]


class ChatCompletionMessageParam(TypedDict, total=False):
    """Describes the structure of a `Message` object."""

    content: Union[str, list[dict]]
    role: Union[Literal["system"], Literal["user"], Literal["assistant"]]


_UNSUPPORTED_ARGUMENT_ERROR_TEMPLATE = (
    "The '{}' argument is not supported by the xAI API. Please remove it from the"
    "`completions.create` call."
)

_UNSUPPORTED_CONTENT_TYPE_ERROR_TEMPLATE = (
    "The '{}' content type is not supported by the xAI API. Please remove it."
)


class Chat:
    """Exposes synchronous Chat APIs."""

    def __init__(self, client: compat_chat_pb2_grpc.ChatStub):
        """Initializes a new instance of the `Chat` class.

        Args:
            client: The synchronous gRPC client to use.
        """
        self.completions = Completions(client)


# Technically, we don't have to map the return types to "native" Python types. However, most
# developers are more familiar with dataclasses than with protos. So we redefine all protos as
# simple dataclasses here.


@dataclasses.dataclass
class ChatCompletionMessage:
    content: str
    role: str

    @classmethod
    def from_proto(cls, proto: compat_chat_pb2.Message):
        """Creates a new instance from a proto message."""
        return ChatCompletionMessage(content=proto.content, role=proto.role)


@dataclasses.dataclass
class Choice:
    finish_reason: str
    index: int
    message: ChatCompletionMessage

    @classmethod
    def from_proto(cls, proto: compat_chat_pb2.Choice):
        """Creates a new instance from a proto message."""
        return Choice(
            finish_reason=proto.finish_reason,
            index=proto.index,
            message=ChatCompletionMessage.from_proto(proto.message),
        )


@dataclasses.dataclass
class CompletionUsage:
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

    @classmethod
    def from_proto(cls, proto: compat_chat_pb2.Usage):
        """Creates a new instance from a proto message."""
        return CompletionUsage(
            completion_tokens=proto.completion_tokens,
            prompt_tokens=proto.completion_tokens,
            total_tokens=proto.total_tokens,
        )


@dataclasses.dataclass
class ChatCompletion:
    id: str
    choices: list[Choice]
    created: int
    model: str
    object: str
    system_fingerprint: Optional[str] = None
    usage: Optional[CompletionUsage] = None

    @classmethod
    def from_proto(cls, proto: compat_chat_pb2.GetChatCompletionResponse):
        """Creates a new instance from a proto message."""
        return ChatCompletion(
            id=proto.id,
            choices=[Choice.from_proto(c) for c in proto.choices],
            created=proto.created,
            model=proto.model,
            object=proto.object,
            system_fingerprint=proto.system_fingerprint,
            usage=CompletionUsage.from_proto(proto.usage) if proto.usage is not None else None,
        )


@dataclasses.dataclass
class ChoiceDelta:
    content: Optional[str] = None
    role: Optional[str] = None

    @classmethod
    def from_proto(cls, proto: compat_chat_pb2.Delta):
        """Creates a new instance from a proto message."""
        return ChoiceDelta(content=proto.content, role=proto.role)


@dataclasses.dataclass
class ChoiceChunk:
    delta: ChoiceDelta
    finish_reason: str
    index: int

    @classmethod
    def from_proto(cls, proto: compat_chat_pb2.ChoiceChunk):
        """Creates a new instance from a proto message."""
        return ChoiceChunk(
            delta=ChoiceDelta.from_proto(proto.delta),
            finish_reason=proto.finish_reason,
            index=proto.index,
        )


@dataclasses.dataclass
class ChatCompletionChunk:
    id: str
    choices: list[ChoiceChunk]
    created: int
    model: str
    object: str
    system_fingerprint: Optional[str] = None

    @classmethod
    def from_proto(cls, proto: compat_chat_pb2.GetChatCompletionChunk):
        """Creates a new instance from a proto message."""
        return ChatCompletionChunk(
            id=proto.id,
            choices=[ChoiceChunk.from_proto(c) for c in proto.choices],
            created=proto.created,
            model=proto.model,
            object=proto.object,
            system_fingerprint=proto.system_fingerprint,
        )


class Completions:
    """Implements a synchronous chat completions API."""

    def __init__(self, client: compat_chat_pb2_grpc.ChatStub):
        """Initializes a new instance of the `Completions` class.

        Args:
            client: The synchronous gRPC client to use.
        """
        self._client = client

    def create(
        self,
        *,
        messages: list[ChatCompletionMessageParam],
        model: Optional[str] = None,
        frequency_penalty: Optional[float] = None,
        function_call: Any = None,
        functions: Any = None,
        logit_bias: Optional[dict[str, int]] = None,
        max_tokens: Optional[int] = None,
        n: Optional[int] = None,
        presence_penalty: Optional[float] = None,
        response_format: Optional[ResponseFormat] = None,
        seed: Optional[int] = None,
        stop: Union[Optional[str], list[str]] = None,
        stream: Optional[bool] = None,
        temperature: Optional[float] = None,
        tool_choice: Any = None,
        tools: Any = None,
        top_p: Optional[float] = None,
        user: Optional[str] = None,
        extra_headers: Any = None,
        extra_query: Any = None,
        extra_body: Any = None,
        timeout: Optional[float] = None,
    ) -> Union[ChatCompletion, Generator[ChatCompletionChunk, None, None]]:
        """Creates a new chat completion by calling the API.

        Args:
            messages: List of messages that have been exchanged in the conversation (i.e. the
                message history).
            model: ID of the model to sample from. If empty/not provided, the default model will be
                used.
            frequency_penalty: Discourages the model from repeating the same answer again by
                decreasing the probability of tokens proportionally to the number of times they were
                sampled.
            function_call: Not supported. Only added for API compatibility.
            functions: Not supported. Only added for API compatibility.
            logit_bias: A bias value that is added to the network outputs. It's a mapping from token
                ID to a numeric bias.
            max_tokens: Maximum number of tokens to sample from the model.
            n: Number of concurrent completions to generate.
            presence_penalty: Discourages the model from repeating the same answer again by
                decreasing the probability of tokens that have been sampled already.
            response_format: Object specifying the response format to use.
            seed: Random number generator seed to use. Makes sampling deterministic.
            stop: A sequence of stop strings. If any of these strings is observed in the model's
                output, sampling is stopped afterward.
            stream: If true, the function returns a stream of chunks instead of waiting for the
                entire response to finish before returning.
            temperature: Controls the sampling temperature. The smaller the value, the less varied
                answers become.
            tool_choice: Not supported. Only added for API compatibility.
            tools: Not supported. Only added for API compatibility.
            top_p: Sampling threshold of the nucleus sampling algorith. Only token within the top-p
                percentile will be considered for sampling.
            user: An opaque string used in the backend to associate the request with. Can be useful
                for detecting abuse.
            extra_headers: Not supported. Only added for API compatibility.
            extra_query: Not supported. Only added for API compatibility.
            extra_body: Not supported. Only added for API compatibility.
            timeout: Maximum request time before a Timeout exception is raised.

        Returns:
            Either a completion or a stream of chunks if `stream=True`.
        """
        # We raise descriptive error message if an unsupported argument was passed. This makes will
        # be easier to interpret than getting an "undefined argument"-type error.
        unsupported = {
            "function_call": function_call,
            "functions": functions,
            "tool_choice": tool_choice,
            "tools": tools,
            "extra_headers": extra_headers,
            "extra_query": extra_query,
            "extra_bod": extra_body,
        }
        for name, value in unsupported.items():
            if value is not None:
                raise ValueError(_UNSUPPORTED_ARGUMENT_ERROR_TEMPLATE.format(name))

        # The gRPC API only supports an array of stop strings. If a single string was provided, wrap
        # it in a list.
        if isinstance(stop, str):
            stop = [stop]

        # Convert the response-format object to a proto.
        if response_format is not None:
            response_format = compat_chat_pb2.ResponseFormat(type=response_format["type"])

        def _parse_message(message):
            content = None
            if isinstance(message["content"], str):
                content = [
                    compat_chat_pb2.Content(
                        type="text",
                        text=message["content"],
                    )
                ]
            elif isinstance(message["content"], list):
                content = []
                for content_dict in message["content"]:
                    content_type = content_dict["type"]
                    if content_type in ["text", "text_file"]:
                        content.append(
                            compat_chat_pb2.Content(
                                type=content_type,
                                text=content_dict["text"],
                            )
                        )
                    elif content_type == "image_url":
                        content.append(
                            compat_chat_pb2.Content(
                                type=content_type,
                                image_url=compat_chat_pb2.ImageUrl(
                                    url=content_dict["image_url"]["url"]
                                ),
                            )
                        )
                    else:
                        raise ValueError(
                            _UNSUPPORTED_CONTENT_TYPE_ERROR_TEMPLATE.format(content_type)
                        )
            else:
                raise ValueError("Content must be either a string or a list of dictionary.")

            return compat_chat_pb2.Message(
                content=content,
                role=message["role"],
            )

        # Create the request proto.
        request = compat_chat_pb2.GetCompletionsRequest(
            messages=map(_parse_message, messages),
            model=model or "",
            frequency_penalty=frequency_penalty or 0,
            logit_bias=logit_bias,
            max_tokens=max_tokens or 128,
            n=n or 1,
            presence_penalty=presence_penalty or 0,
            response_format=response_format,
            seed=seed or random.randint(1, 10000),
            stop=stop,
            temperature=temperature or 0.7,
            top_p=top_p or 0.95,
            user=user or "",
        )

        kwargs = {}
        if timeout is not None:
            kwargs["timeout"] = timeout

        if stream:

            def _unroll():
                """Unrolls the stream so we can return an iterator"""
                for chunk in self._client.GetCompletionChunk(request):
                    yield ChatCompletionChunk.from_proto(chunk)

            return _unroll()
        else:
            return ChatCompletion.from_proto(self._client.GetCompletion(request, **kwargs))
