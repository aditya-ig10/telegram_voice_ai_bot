from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from . import x_entities_pb2 as _x_entities_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetXCuratedTrendsRequest(_message.Message):
    __slots__ = ["limit", "category"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    limit: int
    category: str
    def __init__(self, limit: _Optional[int] = ..., category: _Optional[str] = ...) -> None: ...

class GetXCuratedTrendsResponse(_message.Message):
    __slots__ = ["trends"]
    TRENDS_FIELD_NUMBER: _ClassVar[int]
    trends: _containers.RepeatedCompositeFieldContainer[_x_entities_pb2.XTrendResult]
    def __init__(self, trends: _Optional[_Iterable[_Union[_x_entities_pb2.XTrendResult, _Mapping]]] = ...) -> None: ...

class GetXTrendByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetXTrendByIdResponse(_message.Message):
    __slots__ = ["trend"]
    TREND_FIELD_NUMBER: _ClassVar[int]
    trend: _x_entities_pb2.XTrendResult
    def __init__(self, trend: _Optional[_Union[_x_entities_pb2.XTrendResult, _Mapping]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ["query", "force_refresh", "model_name", "prompt", "search_id", "backend_address", "force_rust", "image_generator"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    BACKEND_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FORCE_RUST_FIELD_NUMBER: _ClassVar[int]
    IMAGE_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    query: str
    force_refresh: bool
    model_name: str
    prompt: str
    search_id: str
    backend_address: str
    force_rust: bool
    image_generator: str
    def __init__(self, query: _Optional[str] = ..., force_refresh: bool = ..., model_name: _Optional[str] = ..., prompt: _Optional[str] = ..., search_id: _Optional[str] = ..., backend_address: _Optional[str] = ..., force_rust: bool = ..., image_generator: _Optional[str] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ["x_search_results", "web_search_results", "text", "image_generation_results", "x_trend_results", "search_id", "debug"]
    X_SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    WEB_SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_GENERATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    X_TREND_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    x_search_results: XSearchResults
    web_search_results: WebSearchResults
    text: str
    image_generation_results: ImageGenerationResults
    x_trend_results: XTrendResults
    search_id: str
    debug: DebugInformation
    def __init__(self, x_search_results: _Optional[_Union[XSearchResults, _Mapping]] = ..., web_search_results: _Optional[_Union[WebSearchResults, _Mapping]] = ..., text: _Optional[str] = ..., image_generation_results: _Optional[_Union[ImageGenerationResults, _Mapping]] = ..., x_trend_results: _Optional[_Union[XTrendResults, _Mapping]] = ..., search_id: _Optional[str] = ..., debug: _Optional[_Union[DebugInformation, _Mapping]] = ...) -> None: ...

class XSearchResults(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_x_entities_pb2.XPost]
    def __init__(self, results: _Optional[_Iterable[_Union[_x_entities_pb2.XPost, _Mapping]]] = ...) -> None: ...

class XTrendResults(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_x_entities_pb2.XTrendResult]
    def __init__(self, results: _Optional[_Iterable[_Union[_x_entities_pb2.XTrendResult, _Mapping]]] = ...) -> None: ...

class WebSearchResult(_message.Message):
    __slots__ = ["url", "title", "preview", "search_engine_text", "description", "site_name", "metadata_title", "creator", "image", "favicon", "citation_id"]
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ENGINE_TEXT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_TITLE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    FAVICON_FIELD_NUMBER: _ClassVar[int]
    CITATION_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    title: str
    preview: str
    search_engine_text: str
    description: str
    site_name: str
    metadata_title: str
    creator: str
    image: str
    favicon: str
    citation_id: str
    def __init__(self, url: _Optional[str] = ..., title: _Optional[str] = ..., preview: _Optional[str] = ..., search_engine_text: _Optional[str] = ..., description: _Optional[str] = ..., site_name: _Optional[str] = ..., metadata_title: _Optional[str] = ..., creator: _Optional[str] = ..., image: _Optional[str] = ..., favicon: _Optional[str] = ..., citation_id: _Optional[str] = ...) -> None: ...

class WebSearchResults(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[WebSearchResult]
    def __init__(self, results: _Optional[_Iterable[_Union[WebSearchResult, _Mapping]]] = ...) -> None: ...

class ImageGenerationResult(_message.Message):
    __slots__ = ["image_url", "prompt"]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    prompt: str
    def __init__(self, image_url: _Optional[str] = ..., prompt: _Optional[str] = ...) -> None: ...

class ImageGenerationResults(_message.Message):
    __slots__ = ["results", "image_generator"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ImageGenerationResult]
    image_generator: str
    def __init__(self, results: _Optional[_Iterable[_Union[ImageGenerationResult, _Mapping]]] = ..., image_generator: _Optional[str] = ...) -> None: ...

class GetMostRecentSearchQueryRequest(_message.Message):
    __slots__ = ["limit", "query_prefix"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUERY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    limit: int
    query_prefix: str
    def __init__(self, limit: _Optional[int] = ..., query_prefix: _Optional[str] = ...) -> None: ...

class SearchQuery(_message.Message):
    __slots__ = ["search_id", "query"]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    search_id: str
    query: str
    def __init__(self, search_id: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...

class SearchQueryResponse(_message.Message):
    __slots__ = ["queries"]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    queries: _containers.RepeatedCompositeFieldContainer[SearchQuery]
    def __init__(self, queries: _Optional[_Iterable[_Union[SearchQuery, _Mapping]]] = ...) -> None: ...

class DeleteSearchQueryRequest(_message.Message):
    __slots__ = ["search_id"]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    search_id: str
    def __init__(self, search_id: _Optional[str] = ...) -> None: ...

class CompleteQueryRequest(_message.Message):
    __slots__ = ["query"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class CompleteQueryResponse(_message.Message):
    __slots__ = ["query"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class SummarizeWebResultRequest(_message.Message):
    __slots__ = ["query", "url", "backend_address"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BACKEND_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    query: str
    url: str
    backend_address: str
    def __init__(self, query: _Optional[str] = ..., url: _Optional[str] = ..., backend_address: _Optional[str] = ...) -> None: ...

class SummarizeWebResultResponse(_message.Message):
    __slots__ = ["answer"]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    answer: str
    def __init__(self, answer: _Optional[str] = ...) -> None: ...

class WebsiteDebugInformation(_message.Message):
    __slots__ = ["url", "raw_html", "parsed_text", "summarized_chunks"]
    URL_FIELD_NUMBER: _ClassVar[int]
    RAW_HTML_FIELD_NUMBER: _ClassVar[int]
    PARSED_TEXT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZED_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    url: str
    raw_html: str
    parsed_text: str
    summarized_chunks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, url: _Optional[str] = ..., raw_html: _Optional[str] = ..., parsed_text: _Optional[str] = ..., summarized_chunks: _Optional[_Iterable[str]] = ...) -> None: ...

class DebugInformation(_message.Message):
    __slots__ = ["formatted_model_prompt", "websites"]
    FORMATTED_MODEL_PROMPT_FIELD_NUMBER: _ClassVar[int]
    WEBSITES_FIELD_NUMBER: _ClassVar[int]
    formatted_model_prompt: str
    websites: _containers.RepeatedCompositeFieldContainer[WebsiteDebugInformation]
    def __init__(self, formatted_model_prompt: _Optional[str] = ..., websites: _Optional[_Iterable[_Union[WebsiteDebugInformation, _Mapping]]] = ...) -> None: ...
