from .google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SampleTokensRequest(_message.Message):
    __slots__ = ["prompt", "inputs", "settings", "return_attention", "model_name"]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ATTENTION_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    prompt: _containers.RepeatedScalarFieldContainer[int]
    inputs: _containers.RepeatedCompositeFieldContainer[PromptInput]
    settings: SampleSettings
    return_attention: bool
    model_name: str
    def __init__(self, prompt: _Optional[_Iterable[int]] = ..., inputs: _Optional[_Iterable[_Union[PromptInput, _Mapping]]] = ..., settings: _Optional[_Union[SampleSettings, _Mapping]] = ..., return_attention: bool = ..., model_name: _Optional[str] = ...) -> None: ...

class PromptInput(_message.Message):
    __slots__ = ["text", "image_bytes", "image_base64", "token_ids"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BASE64_FIELD_NUMBER: _ClassVar[int]
    TOKEN_IDS_FIELD_NUMBER: _ClassVar[int]
    text: str
    image_bytes: bytes
    image_base64: str
    token_ids: TokenIds
    def __init__(self, text: _Optional[str] = ..., image_bytes: _Optional[bytes] = ..., image_base64: _Optional[str] = ..., token_ids: _Optional[_Union[TokenIds, _Mapping]] = ...) -> None: ...

class TokenIds(_message.Message):
    __slots__ = ["tokens"]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tokens: _Optional[_Iterable[int]] = ...) -> None: ...

class SampleTokensResponse(_message.Message):
    __slots__ = ["token", "budget", "transaction"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    token: Token
    budget: TokenBudget
    transaction: TokenTransaction
    def __init__(self, token: _Optional[_Union[Token, _Mapping]] = ..., budget: _Optional[_Union[TokenBudget, _Mapping]] = ..., transaction: _Optional[_Union[TokenTransaction, _Mapping]] = ...) -> None: ...

class TokenizeAndSampleTokensRequest(_message.Message):
    __slots__ = ["text", "settings", "return_attention", "model_name"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RETURN_ATTENTION_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    text: str
    settings: SampleSettings
    return_attention: bool
    model_name: str
    def __init__(self, text: _Optional[str] = ..., settings: _Optional[_Union[SampleSettings, _Mapping]] = ..., return_attention: bool = ..., model_name: _Optional[str] = ...) -> None: ...

class SampleSettings(_message.Message):
    __slots__ = ["max_len", "temperature", "nucleus_p", "stop_tokens", "stop_strings", "rng_seed", "allowed_tokens", "disallowed_tokens"]
    MAX_LEN_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    NUCLEUS_P_FIELD_NUMBER: _ClassVar[int]
    STOP_TOKENS_FIELD_NUMBER: _ClassVar[int]
    STOP_STRINGS_FIELD_NUMBER: _ClassVar[int]
    RNG_SEED_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    DISALLOWED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    max_len: int
    temperature: float
    nucleus_p: float
    stop_tokens: _containers.RepeatedScalarFieldContainer[str]
    stop_strings: _containers.RepeatedScalarFieldContainer[str]
    rng_seed: int
    allowed_tokens: _containers.RepeatedCompositeFieldContainer[InputToken]
    disallowed_tokens: _containers.RepeatedCompositeFieldContainer[InputToken]
    def __init__(self, max_len: _Optional[int] = ..., temperature: _Optional[float] = ..., nucleus_p: _Optional[float] = ..., stop_tokens: _Optional[_Iterable[str]] = ..., stop_strings: _Optional[_Iterable[str]] = ..., rng_seed: _Optional[int] = ..., allowed_tokens: _Optional[_Iterable[_Union[InputToken, _Mapping]]] = ..., disallowed_tokens: _Optional[_Iterable[_Union[InputToken, _Mapping]]] = ...) -> None: ...

class InputToken(_message.Message):
    __slots__ = ["string_token", "token_id"]
    STRING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    string_token: str
    token_id: int
    def __init__(self, string_token: _Optional[str] = ..., token_id: _Optional[int] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ["final_logit", "top_k", "attention", "token_type"]
    class TokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN: _ClassVar[Token.TokenType]
        USER: _ClassVar[Token.TokenType]
        MODEL: _ClassVar[Token.TokenType]
    UNKNOWN: Token.TokenType
    USER: Token.TokenType
    MODEL: Token.TokenType
    FINAL_LOGIT_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    ATTENTION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    final_logit: Logit
    top_k: _containers.RepeatedCompositeFieldContainer[Logit]
    attention: _containers.RepeatedScalarFieldContainer[float]
    token_type: Token.TokenType
    def __init__(self, final_logit: _Optional[_Union[Logit, _Mapping]] = ..., top_k: _Optional[_Iterable[_Union[Logit, _Mapping]]] = ..., attention: _Optional[_Iterable[float]] = ..., token_type: _Optional[_Union[Token.TokenType, str]] = ...) -> None: ...

class Logit(_message.Message):
    __slots__ = ["token_id", "string_token", "prob"]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    STRING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROB_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    string_token: str
    prob: float
    def __init__(self, token_id: _Optional[int] = ..., string_token: _Optional[str] = ..., prob: _Optional[float] = ...) -> None: ...

class TokenizeRequest(_message.Message):
    __slots__ = ["text", "model_name"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    text: str
    model_name: str
    def __init__(self, text: _Optional[str] = ..., model_name: _Optional[str] = ...) -> None: ...

class TokenizeResponse(_message.Message):
    __slots__ = ["tokens"]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[Token]
    def __init__(self, tokens: _Optional[_Iterable[_Union[Token, _Mapping]]] = ...) -> None: ...

class ListTransactionsResponse(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[TokenTransaction]
    def __init__(self, transactions: _Optional[_Iterable[_Union[TokenTransaction, _Mapping]]] = ...) -> None: ...

class TokenTransaction(_message.Message):
    __slots__ = ["num_prompt_tokens", "num_generated_tokens", "cost_multiplier", "create_time", "transaction_type", "transaction_id", "model_name", "confirmed"]
    NUM_PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    NUM_GENERATED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COST_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    num_prompt_tokens: int
    num_generated_tokens: int
    cost_multiplier: int
    create_time: _timestamp_pb2.Timestamp
    transaction_type: str
    transaction_id: str
    model_name: str
    confirmed: bool
    def __init__(self, num_prompt_tokens: _Optional[int] = ..., num_generated_tokens: _Optional[int] = ..., cost_multiplier: _Optional[int] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., transaction_type: _Optional[str] = ..., transaction_id: _Optional[str] = ..., model_name: _Optional[str] = ..., confirmed: bool = ...) -> None: ...

class GetTokenBudgetRequest(_message.Message):
    __slots__ = ["transaction_type"]
    TRANSACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    transaction_type: str
    def __init__(self, transaction_type: _Optional[str] = ...) -> None: ...

class TokenBudget(_message.Message):
    __slots__ = ["token_limit", "tokens_spent", "request_limit", "requests_spent"]
    TOKEN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_SPENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_LIMIT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_SPENT_FIELD_NUMBER: _ClassVar[int]
    token_limit: int
    tokens_spent: int
    request_limit: int
    requests_spent: int
    def __init__(self, token_limit: _Optional[int] = ..., tokens_spent: _Optional[int] = ..., request_limit: _Optional[int] = ..., requests_spent: _Optional[int] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ["model_names"]
    MODEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    model_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model_names: _Optional[_Iterable[str]] = ...) -> None: ...
