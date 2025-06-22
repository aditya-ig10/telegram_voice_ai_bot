from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Modality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INVALID: _ClassVar[Modality]
    TEXT: _ClassVar[Modality]
    IMAGE: _ClassVar[Modality]
INVALID: Modality
TEXT: Modality
IMAGE: Modality

class GetLanguageModelRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetEmbeddingModelRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class LanguageModel(_message.Message):
    __slots__ = ["name", "version", "input_modalities", "output_modalities", "prompt_text_token_price", "prompt_image_token_price", "completion_text_token_price"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INPUT_MODALITIES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODALITIES_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEXT_TOKEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_IMAGE_TOKEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TEXT_TOKEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    input_modalities: _containers.RepeatedScalarFieldContainer[Modality]
    output_modalities: _containers.RepeatedScalarFieldContainer[Modality]
    prompt_text_token_price: int
    prompt_image_token_price: int
    completion_text_token_price: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., input_modalities: _Optional[_Iterable[_Union[Modality, str]]] = ..., output_modalities: _Optional[_Iterable[_Union[Modality, str]]] = ..., prompt_text_token_price: _Optional[int] = ..., prompt_image_token_price: _Optional[int] = ..., completion_text_token_price: _Optional[int] = ...) -> None: ...

class ListLanguageModelsResponse(_message.Message):
    __slots__ = ["models"]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[LanguageModel]
    def __init__(self, models: _Optional[_Iterable[_Union[LanguageModel, _Mapping]]] = ...) -> None: ...

class EmbeddingModel(_message.Message):
    __slots__ = ["name", "version", "input_modalities", "prompt_text_token_price", "prompt_image_token_price"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INPUT_MODALITIES_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TEXT_TOKEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    PROMPT_IMAGE_TOKEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    input_modalities: _containers.RepeatedScalarFieldContainer[Modality]
    prompt_text_token_price: int
    prompt_image_token_price: int
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., input_modalities: _Optional[_Iterable[_Union[Modality, str]]] = ..., prompt_text_token_price: _Optional[int] = ..., prompt_image_token_price: _Optional[int] = ...) -> None: ...

class ListEmbeddingModelsResponse(_message.Message):
    __slots__ = ["models"]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[EmbeddingModel]
    def __init__(self, models: _Optional[_Iterable[_Union[EmbeddingModel, _Mapping]]] = ...) -> None: ...
