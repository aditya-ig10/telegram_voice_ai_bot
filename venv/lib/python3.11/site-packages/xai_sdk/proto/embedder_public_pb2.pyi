from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmbedRequest(_message.Message):
    __slots__ = ["texts", "model_name"]
    TEXTS_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    texts: _containers.RepeatedScalarFieldContainer[str]
    model_name: str
    def __init__(self, texts: _Optional[_Iterable[str]] = ..., model_name: _Optional[str] = ...) -> None: ...

class EmbedResponse(_message.Message):
    __slots__ = ["embeddings"]
    EMBEDDINGS_FIELD_NUMBER: _ClassVar[int]
    embeddings: _containers.RepeatedCompositeFieldContainer[Embedding]
    def __init__(self, embeddings: _Optional[_Iterable[_Union[Embedding, _Mapping]]] = ...) -> None: ...

class Embedding(_message.Message):
    __slots__ = ["values", "shape"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    shape: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, values: _Optional[_Iterable[float]] = ..., shape: _Optional[_Iterable[int]] = ...) -> None: ...
