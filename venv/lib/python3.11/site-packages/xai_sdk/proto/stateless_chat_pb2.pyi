from .google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from . import chat_pb2 as _chat_pb2
from . import prod_search_pb2 as _prod_search_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatelessConversation(_message.Message):
    __slots__ = ["stateless_conversation_id", "responses", "system_prompt_name", "name", "username", "expose_username_to_grok", "disable_search", "enable_image_generation", "model_name", "x_posts_as_field", "additional_options"]
    STATELESS_CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EXPOSE_USERNAME_TO_GROK_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_IMAGE_GENERATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    X_POSTS_AS_FIELD_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    stateless_conversation_id: str
    responses: _containers.RepeatedCompositeFieldContainer[StatelessResponse]
    system_prompt_name: str
    name: str
    username: str
    expose_username_to_grok: bool
    disable_search: bool
    enable_image_generation: bool
    model_name: str
    x_posts_as_field: bool
    additional_options: _chat_pb2.AdditionalOptions
    def __init__(self, stateless_conversation_id: _Optional[str] = ..., responses: _Optional[_Iterable[_Union[StatelessResponse, _Mapping]]] = ..., system_prompt_name: _Optional[str] = ..., name: _Optional[str] = ..., username: _Optional[str] = ..., expose_username_to_grok: bool = ..., disable_search: bool = ..., enable_image_generation: bool = ..., model_name: _Optional[str] = ..., x_posts_as_field: bool = ..., additional_options: _Optional[_Union[_chat_pb2.AdditionalOptions, _Mapping]] = ...) -> None: ...

class StatelessResponse(_message.Message):
    __slots__ = ["sender", "message", "query", "query_type", "image_attachment", "x_post_ids", "debug_log", "image_inputs", "web_search_results", "search_context"]
    class Sender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[StatelessResponse.Sender]
        HUMAN: _ClassVar[StatelessResponse.Sender]
        ASSISTANT: _ClassVar[StatelessResponse.Sender]
    UNKNOWN: StatelessResponse.Sender
    HUMAN: StatelessResponse.Sender
    ASSISTANT: StatelessResponse.Sender
    SENDER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    X_POST_IDS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_LOG_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INPUTS_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    sender: StatelessResponse.Sender
    message: str
    query: str
    query_type: str
    image_attachment: ImageAttachment
    x_post_ids: _containers.RepeatedScalarFieldContainer[str]
    debug_log: _chat_pb2.ResponseDebugLog
    image_inputs: _containers.RepeatedScalarFieldContainer[str]
    web_search_results: _prod_search_pb2.WebSearchResults
    search_context: _chat_pb2.SearchContext
    def __init__(self, sender: _Optional[_Union[StatelessResponse.Sender, str]] = ..., message: _Optional[str] = ..., query: _Optional[str] = ..., query_type: _Optional[str] = ..., image_attachment: _Optional[_Union[ImageAttachment, _Mapping]] = ..., x_post_ids: _Optional[_Iterable[str]] = ..., debug_log: _Optional[_Union[_chat_pb2.ResponseDebugLog, _Mapping]] = ..., image_inputs: _Optional[_Iterable[str]] = ..., web_search_results: _Optional[_Union[_prod_search_pb2.WebSearchResults, _Mapping]] = ..., search_context: _Optional[_Union[_chat_pb2.SearchContext, _Mapping]] = ...) -> None: ...

class ImageAttachment(_message.Message):
    __slots__ = ["image_bytes", "content_type", "image_url"]
    IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    image_bytes: bytes
    content_type: str
    image_url: str
    def __init__(self, image_bytes: _Optional[bytes] = ..., content_type: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...

class DeleteLoggedConversationsRequest(_message.Message):
    __slots__ = ["accounting_key"]
    ACCOUNTING_KEY_FIELD_NUMBER: _ClassVar[int]
    accounting_key: str
    def __init__(self, accounting_key: _Optional[str] = ...) -> None: ...
