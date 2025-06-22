from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class XPost(_message.Message):
    __slots__ = ["username", "name", "text", "create_time", "profile_image_url", "post_id", "citation_id", "parent", "parent_post_id", "quote_post_id", "quote"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    CITATION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_POST_ID_FIELD_NUMBER: _ClassVar[int]
    QUOTE_POST_ID_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    username: str
    name: str
    text: str
    create_time: _timestamp_pb2.Timestamp
    profile_image_url: str
    post_id: str
    citation_id: str
    parent: XPost
    parent_post_id: str
    quote_post_id: str
    quote: XPost
    def __init__(self, username: _Optional[str] = ..., name: _Optional[str] = ..., text: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., profile_image_url: _Optional[str] = ..., post_id: _Optional[str] = ..., citation_id: _Optional[str] = ..., parent: _Optional[_Union[XPost, _Mapping]] = ..., parent_post_id: _Optional[str] = ..., quote_post_id: _Optional[str] = ..., quote: _Optional[_Union[XPost, _Mapping]] = ...) -> None: ...

class XTrendPost(_message.Message):
    __slots__ = ["author_handle", "author_name", "author_avatar", "author_nfollowers", "rest_id", "nreplies", "text", "created_ts", "nreposts", "imgs", "vids", "card"]
    AUTHOR_HANDLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_AVATAR_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NFOLLOWERS_FIELD_NUMBER: _ClassVar[int]
    REST_ID_FIELD_NUMBER: _ClassVar[int]
    NREPLIES_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CREATED_TS_FIELD_NUMBER: _ClassVar[int]
    NREPOSTS_FIELD_NUMBER: _ClassVar[int]
    IMGS_FIELD_NUMBER: _ClassVar[int]
    VIDS_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    author_handle: str
    author_name: str
    author_avatar: str
    author_nfollowers: int
    rest_id: str
    nreplies: int
    text: str
    created_ts: int
    nreposts: int
    imgs: _containers.RepeatedScalarFieldContainer[str]
    vids: _containers.RepeatedScalarFieldContainer[str]
    card: XTrendPostCard
    def __init__(self, author_handle: _Optional[str] = ..., author_name: _Optional[str] = ..., author_avatar: _Optional[str] = ..., author_nfollowers: _Optional[int] = ..., rest_id: _Optional[str] = ..., nreplies: _Optional[int] = ..., text: _Optional[str] = ..., created_ts: _Optional[int] = ..., nreposts: _Optional[int] = ..., imgs: _Optional[_Iterable[str]] = ..., vids: _Optional[_Iterable[str]] = ..., card: _Optional[_Union[XTrendPostCard, _Mapping]] = ...) -> None: ...

class XTrendResult(_message.Message):
    __slots__ = ["name", "hook", "summary", "rest_id", "posts", "thumbnail", "header"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    REST_ID_FIELD_NUMBER: _ClassVar[int]
    POSTS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    name: str
    hook: str
    summary: str
    rest_id: str
    posts: _containers.RepeatedCompositeFieldContainer[XTrendPost]
    thumbnail: str
    header: str
    def __init__(self, name: _Optional[str] = ..., hook: _Optional[str] = ..., summary: _Optional[str] = ..., rest_id: _Optional[str] = ..., posts: _Optional[_Iterable[_Union[XTrendPost, _Mapping]]] = ..., thumbnail: _Optional[str] = ..., header: _Optional[str] = ...) -> None: ...

class XTrendPostCard(_message.Message):
    __slots__ = ["img", "url"]
    IMG_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    img: str
    url: str
    def __init__(self, img: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
