from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import sampler_public_pb2 as _sampler_public_pb2
from . import prod_search_pb2 as _prod_search_pb2
from . import x_entities_pb2 as _x_entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegenerateResponseRequest(_message.Message):
    __slots__ = ["conversation_id", "response_id"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    response_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., response_id: _Optional[str] = ...) -> None: ...

class CreateConversationRequest(_message.Message):
    __slots__ = ["system_prompt_name"]
    SYSTEM_PROMPT_NAME_FIELD_NUMBER: _ClassVar[int]
    system_prompt_name: str
    def __init__(self, system_prompt_name: _Optional[str] = ...) -> None: ...

class GetConversationRequest(_message.Message):
    __slots__ = ["conversation_id"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    def __init__(self, conversation_id: _Optional[str] = ...) -> None: ...

class DeleteConversationRequest(_message.Message):
    __slots__ = ["conversation_id"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    def __init__(self, conversation_id: _Optional[str] = ...) -> None: ...

class ListConversationsRequest(_message.Message):
    __slots__ = ["page_size", "next_page_token"]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    next_page_token: str
    def __init__(self, page_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListConversationsResponse(_message.Message):
    __slots__ = ["conversations"]
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    def __init__(self, conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]] = ...) -> None: ...

class GenerateTitleRequest(_message.Message):
    __slots__ = ["conversation_id", "leaf_response_id"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    LEAF_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    leaf_response_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., leaf_response_id: _Optional[str] = ...) -> None: ...

class GenerateTitleResponse(_message.Message):
    __slots__ = ["new_title"]
    NEW_TITLE_FIELD_NUMBER: _ClassVar[int]
    new_title: str
    def __init__(self, new_title: _Optional[str] = ...) -> None: ...

class AddModelResponseRequest(_message.Message):
    __slots__ = ["conversation_id", "message", "partial", "parent_response_id"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    PARENT_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    message: str
    partial: bool
    parent_response_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., message: _Optional[str] = ..., partial: bool = ..., parent_response_id: _Optional[str] = ...) -> None: ...

class UpdateConversationRequest(_message.Message):
    __slots__ = ["conversation_id", "title", "starred"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STARRED_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    title: str
    starred: bool
    def __init__(self, conversation_id: _Optional[str] = ..., title: _Optional[str] = ..., starred: bool = ...) -> None: ...

class SearchContext(_message.Message):
    __slots__ = ["web_search_query", "web_formatted_chunks", "x_search_query", "x_formatted_chunks", "date"]
    WEB_SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    WEB_FORMATTED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    X_SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    X_FORMATTED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    web_search_query: str
    web_formatted_chunks: str
    x_search_query: str
    x_formatted_chunks: str
    date: str
    def __init__(self, web_search_query: _Optional[str] = ..., web_formatted_chunks: _Optional[str] = ..., x_search_query: _Optional[str] = ..., x_formatted_chunks: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class ResponseDebugLog(_message.Message):
    __slots__ = ["system_prompt_name", "disable_search", "web_query", "x_query", "image_query", "prompt", "inputs", "search_context"]
    SYSTEM_PROMPT_NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    WEB_QUERY_FIELD_NUMBER: _ClassVar[int]
    X_QUERY_FIELD_NUMBER: _ClassVar[int]
    IMAGE_QUERY_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    system_prompt_name: str
    disable_search: bool
    web_query: str
    x_query: str
    image_query: str
    prompt: str
    inputs: _containers.RepeatedCompositeFieldContainer[_sampler_public_pb2.PromptInput]
    search_context: SearchContext
    def __init__(self, system_prompt_name: _Optional[str] = ..., disable_search: bool = ..., web_query: _Optional[str] = ..., x_query: _Optional[str] = ..., image_query: _Optional[str] = ..., prompt: _Optional[str] = ..., inputs: _Optional[_Iterable[_Union[_sampler_public_pb2.PromptInput, _Mapping]]] = ..., search_context: _Optional[_Union[SearchContext, _Mapping]] = ...) -> None: ...

class AdditionalOptions(_message.Message):
    __slots__ = ["injected_search_context", "temperature", "seed", "ignore_time_location", "max_len"]
    INJECTED_SEARCH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    IGNORE_TIME_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAX_LEN_FIELD_NUMBER: _ClassVar[int]
    injected_search_context: SearchContext
    temperature: float
    seed: int
    ignore_time_location: bool
    max_len: int
    def __init__(self, injected_search_context: _Optional[_Union[SearchContext, _Mapping]] = ..., temperature: _Optional[float] = ..., seed: _Optional[int] = ..., ignore_time_location: bool = ..., max_len: _Optional[int] = ...) -> None: ...

class AddResponseRequest(_message.Message):
    __slots__ = ["conversation_id", "message", "model_name", "parent_response_id", "system_prompt_name", "disable_search", "enable_image_generation", "force_rust", "image_attachments", "return_image_bytes", "additional_options"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_IMAGE_GENERATION_FIELD_NUMBER: _ClassVar[int]
    FORCE_RUST_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    RETURN_IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    message: str
    model_name: str
    parent_response_id: str
    system_prompt_name: str
    disable_search: bool
    enable_image_generation: bool
    force_rust: bool
    image_attachments: _containers.RepeatedScalarFieldContainer[str]
    return_image_bytes: bool
    additional_options: AdditionalOptions
    def __init__(self, conversation_id: _Optional[str] = ..., message: _Optional[str] = ..., model_name: _Optional[str] = ..., parent_response_id: _Optional[str] = ..., system_prompt_name: _Optional[str] = ..., disable_search: bool = ..., enable_image_generation: bool = ..., force_rust: bool = ..., image_attachments: _Optional[_Iterable[str]] = ..., return_image_bytes: bool = ..., additional_options: _Optional[_Union[AdditionalOptions, _Mapping]] = ...) -> None: ...

class AddResponseResponse(_message.Message):
    __slots__ = ["user_response", "token", "model_response", "query_action", "image_generation_response", "x_search_results", "cached_image_generation_response", "web_search_results", "search_context"]
    USER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    MODEL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    QUERY_ACTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_GENERATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    X_SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    CACHED_IMAGE_GENERATION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    user_response: Response
    token: _sampler_public_pb2.SampleTokensResponse
    model_response: Response
    query_action: QueryAction
    image_generation_response: ImageGenerationResponse
    x_search_results: _prod_search_pb2.XSearchResults
    cached_image_generation_response: CachedImageGenerationResponse
    web_search_results: _prod_search_pb2.WebSearchResults
    search_context: SearchContext
    def __init__(self, user_response: _Optional[_Union[Response, _Mapping]] = ..., token: _Optional[_Union[_sampler_public_pb2.SampleTokensResponse, _Mapping]] = ..., model_response: _Optional[_Union[Response, _Mapping]] = ..., query_action: _Optional[_Union[QueryAction, _Mapping]] = ..., image_generation_response: _Optional[_Union[ImageGenerationResponse, _Mapping]] = ..., x_search_results: _Optional[_Union[_prod_search_pb2.XSearchResults, _Mapping]] = ..., cached_image_generation_response: _Optional[_Union[CachedImageGenerationResponse, _Mapping]] = ..., web_search_results: _Optional[_Union[_prod_search_pb2.WebSearchResults, _Mapping]] = ..., search_context: _Optional[_Union[SearchContext, _Mapping]] = ...) -> None: ...

class QueryAction(_message.Message):
    __slots__ = ["query", "type"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    query: str
    type: str
    def __init__(self, query: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class Conversation(_message.Message):
    __slots__ = ["conversation_id", "title", "starred", "create_time", "modify_time", "responses", "system_prompt_name"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STARRED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_NAME_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    title: str
    starred: bool
    create_time: _timestamp_pb2.Timestamp
    modify_time: _timestamp_pb2.Timestamp
    responses: _containers.RepeatedCompositeFieldContainer[Response]
    system_prompt_name: str
    def __init__(self, conversation_id: _Optional[str] = ..., title: _Optional[str] = ..., starred: bool = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modify_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., responses: _Optional[_Iterable[_Union[Response, _Mapping]]] = ..., system_prompt_name: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["response_id", "message", "sender", "create_time", "parent_response_id", "manual", "partial", "shared", "query", "query_type", "xpost_ids", "xposts", "generated_image_urls", "debug_log", "image_attachments"]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARENT_RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    XPOST_IDS_FIELD_NUMBER: _ClassVar[int]
    XPOSTS_FIELD_NUMBER: _ClassVar[int]
    GENERATED_IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_LOG_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    response_id: str
    message: str
    sender: str
    create_time: _timestamp_pb2.Timestamp
    parent_response_id: str
    manual: bool
    partial: bool
    shared: bool
    query: str
    query_type: str
    xpost_ids: _containers.RepeatedScalarFieldContainer[str]
    xposts: _containers.RepeatedCompositeFieldContainer[_x_entities_pb2.XPost]
    generated_image_urls: _containers.RepeatedScalarFieldContainer[str]
    debug_log: ResponseDebugLog
    image_attachments: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, response_id: _Optional[str] = ..., message: _Optional[str] = ..., sender: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., parent_response_id: _Optional[str] = ..., manual: bool = ..., partial: bool = ..., shared: bool = ..., query: _Optional[str] = ..., query_type: _Optional[str] = ..., xpost_ids: _Optional[_Iterable[str]] = ..., xposts: _Optional[_Iterable[_Union[_x_entities_pb2.XPost, _Mapping]]] = ..., generated_image_urls: _Optional[_Iterable[str]] = ..., debug_log: _Optional[_Union[ResponseDebugLog, _Mapping]] = ..., image_attachments: _Optional[_Iterable[str]] = ...) -> None: ...

class ImageGenerationResponse(_message.Message):
    __slots__ = ["generated_image_bytes", "content_type"]
    GENERATED_IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    generated_image_bytes: bytes
    content_type: str
    def __init__(self, generated_image_bytes: _Optional[bytes] = ..., content_type: _Optional[str] = ...) -> None: ...

class CachedImageGenerationResponse(_message.Message):
    __slots__ = ["image_url"]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    def __init__(self, image_url: _Optional[str] = ...) -> None: ...

class ShareConversationRequest(_message.Message):
    __slots__ = ["conversation_id", "response_id"]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    conversation_id: str
    response_id: str
    def __init__(self, conversation_id: _Optional[str] = ..., response_id: _Optional[str] = ...) -> None: ...

class ShareConversationResponse(_message.Message):
    __slots__ = ["shared_id"]
    SHARED_ID_FIELD_NUMBER: _ClassVar[int]
    shared_id: str
    def __init__(self, shared_id: _Optional[str] = ...) -> None: ...

class SearchConversationsRequest(_message.Message):
    __slots__ = ["query", "page_size", "next_page_token"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    query: str
    page_size: int
    next_page_token: str
    def __init__(self, query: _Optional[str] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SearchConversationsResponse(_message.Message):
    __slots__ = ["conversations"]
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    def __init__(self, conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]] = ...) -> None: ...
