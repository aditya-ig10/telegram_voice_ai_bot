from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageDetail(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DETAIL_INVALID: _ClassVar[ImageDetail]
    DETAIL_AUTO: _ClassVar[ImageDetail]
    DETAIL_LOW: _ClassVar[ImageDetail]
    DETAIL_HIGH: _ClassVar[ImageDetail]
DETAIL_INVALID: ImageDetail
DETAIL_AUTO: ImageDetail
DETAIL_LOW: ImageDetail
DETAIL_HIGH: ImageDetail

class ImageUrlContent(_message.Message):
    __slots__ = ["image_url", "detail"]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    detail: ImageDetail
    def __init__(self, image_url: _Optional[str] = ..., detail: _Optional[_Union[ImageDetail, str]] = ...) -> None: ...
