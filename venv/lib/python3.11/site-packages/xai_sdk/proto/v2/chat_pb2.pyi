from . import image_pb2 as _image_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INVALID_ROLE: _ClassVar[MessageRole]
    ROLE_USER: _ClassVar[MessageRole]
    ROLE_ASSISTANT: _ClassVar[MessageRole]
    ROLE_SYSTEM: _ClassVar[MessageRole]
    ROLE_FUNCTION: _ClassVar[MessageRole]

class FinishReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REASON_INVALID: _ClassVar[FinishReason]
    REASON_MAX_LEN: _ClassVar[FinishReason]
    REASON_MAX_CONTEXT: _ClassVar[FinishReason]
    REASON_STOP: _ClassVar[FinishReason]
INVALID_ROLE: MessageRole
ROLE_USER: MessageRole
ROLE_ASSISTANT: MessageRole
ROLE_SYSTEM: MessageRole
ROLE_FUNCTION: MessageRole
REASON_INVALID: FinishReason
REASON_MAX_LEN: FinishReason
REASON_MAX_CONTEXT: FinishReason
REASON_STOP: FinishReason

class GetCompletionsRequest(_message.Message):
    __slots__ = ["messages", "model", "user", "n", "max_tokens", "seed", "stop", "temperature", "top_p", "frequency_penalty", "logit_bias", "logprobs", "presence_penalty", "response_format", "top_logprobs"]
    class LogitBiasEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: float
        def __init__(self, key: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    LOGIT_BIAS_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    TOP_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[Message]
    model: str
    user: str
    n: int
    max_tokens: int
    seed: int
    stop: _containers.RepeatedScalarFieldContainer[str]
    temperature: float
    top_p: float
    frequency_penalty: float
    logit_bias: _containers.ScalarMap[int, float]
    logprobs: bool
    presence_penalty: float
    response_format: ResponseFormat
    top_logprobs: int
    def __init__(self, messages: _Optional[_Iterable[_Union[Message, _Mapping]]] = ..., model: _Optional[str] = ..., user: _Optional[str] = ..., n: _Optional[int] = ..., max_tokens: _Optional[int] = ..., seed: _Optional[int] = ..., stop: _Optional[_Iterable[str]] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., frequency_penalty: _Optional[float] = ..., logit_bias: _Optional[_Mapping[int, float]] = ..., logprobs: bool = ..., presence_penalty: _Optional[float] = ..., response_format: _Optional[_Union[ResponseFormat, _Mapping]] = ..., top_logprobs: _Optional[int] = ...) -> None: ...

class GetChatCompletionChunk(_message.Message):
    __slots__ = ["id", "choices", "created", "model", "system_fingerprint", "usage"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    choices: _containers.RepeatedCompositeFieldContainer[ChoiceChunk]
    created: _timestamp_pb2.Timestamp
    model: str
    system_fingerprint: str
    usage: Usage
    def __init__(self, id: _Optional[str] = ..., choices: _Optional[_Iterable[_Union[ChoiceChunk, _Mapping]]] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., model: _Optional[str] = ..., system_fingerprint: _Optional[str] = ..., usage: _Optional[_Union[Usage, _Mapping]] = ...) -> None: ...

class GetChatCompletionResponse(_message.Message):
    __slots__ = ["id", "choices", "created", "model", "system_fingerprint", "usage"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    choices: _containers.RepeatedCompositeFieldContainer[Choice]
    created: _timestamp_pb2.Timestamp
    model: str
    system_fingerprint: str
    usage: Usage
    def __init__(self, id: _Optional[str] = ..., choices: _Optional[_Iterable[_Union[Choice, _Mapping]]] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., model: _Optional[str] = ..., system_fingerprint: _Optional[str] = ..., usage: _Optional[_Union[Usage, _Mapping]] = ...) -> None: ...

class ChoiceChunk(_message.Message):
    __slots__ = ["delta", "logprobs", "finish_reason", "index"]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    delta: Delta
    logprobs: LogProbs
    finish_reason: FinishReason
    index: int
    def __init__(self, delta: _Optional[_Union[Delta, _Mapping]] = ..., logprobs: _Optional[_Union[LogProbs, _Mapping]] = ..., finish_reason: _Optional[_Union[FinishReason, str]] = ..., index: _Optional[int] = ...) -> None: ...

class Delta(_message.Message):
    __slots__ = ["content", "role"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    content: str
    role: MessageRole
    def __init__(self, content: _Optional[str] = ..., role: _Optional[_Union[MessageRole, str]] = ...) -> None: ...

class Choice(_message.Message):
    __slots__ = ["finish_reason", "index", "message", "logprobs"]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    finish_reason: FinishReason
    index: int
    message: CompletionMessage
    logprobs: LogProbs
    def __init__(self, finish_reason: _Optional[_Union[FinishReason, str]] = ..., index: _Optional[int] = ..., message: _Optional[_Union[CompletionMessage, _Mapping]] = ..., logprobs: _Optional[_Union[LogProbs, _Mapping]] = ...) -> None: ...

class CompletionMessage(_message.Message):
    __slots__ = ["content", "role"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    content: str
    role: MessageRole
    def __init__(self, content: _Optional[str] = ..., role: _Optional[_Union[MessageRole, str]] = ...) -> None: ...

class LogProbs(_message.Message):
    __slots__ = ["content"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[LogProb]
    def __init__(self, content: _Optional[_Iterable[_Union[LogProb, _Mapping]]] = ...) -> None: ...

class LogProb(_message.Message):
    __slots__ = ["token", "logprob", "bytes", "top_logprobs"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOGPROB_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    TOP_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    token: str
    logprob: float
    bytes: bytes
    top_logprobs: _containers.RepeatedCompositeFieldContainer[TopLogProb]
    def __init__(self, token: _Optional[str] = ..., logprob: _Optional[float] = ..., bytes: _Optional[bytes] = ..., top_logprobs: _Optional[_Iterable[_Union[TopLogProb, _Mapping]]] = ...) -> None: ...

class Usage(_message.Message):
    __slots__ = ["completion_tokens", "prompt_tokens", "total_tokens", "prompt_text_tokens", "prompt_image_tokens"]
    COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_IMAGE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    prompt_text_tokens: int
    prompt_image_tokens: int
    def __init__(self, completion_tokens: _Optional[int] = ..., prompt_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., prompt_text_tokens: _Optional[int] = ..., prompt_image_tokens: _Optional[int] = ...) -> None: ...

class TopLogProb(_message.Message):
    __slots__ = ["token", "logprob", "bytes"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOGPROB_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    token: str
    logprob: float
    bytes: bytes
    def __init__(self, token: _Optional[str] = ..., logprob: _Optional[float] = ..., bytes: _Optional[bytes] = ...) -> None: ...

class ResponseFormat(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    def __init__(self, type: _Optional[str] = ...) -> None: ...

class Content(_message.Message):
    __slots__ = ["text", "image_url"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    text: str
    image_url: _image_pb2.ImageUrlContent
    def __init__(self, text: _Optional[str] = ..., image_url: _Optional[_Union[_image_pb2.ImageUrlContent, _Mapping]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["content", "role", "name"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[Content]
    role: MessageRole
    name: str
    def __init__(self, content: _Optional[_Iterable[_Union[Content, _Mapping]]] = ..., role: _Optional[_Union[MessageRole, str]] = ..., name: _Optional[str] = ...) -> None: ...
