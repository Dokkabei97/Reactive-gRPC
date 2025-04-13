from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("id", "name", "price", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    price: int
    created_at: str
    updated_at: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., price: _Optional[int] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class CreateProductRequest(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: Product
    def __init__(self, product: _Optional[_Union[Product, _Mapping]] = ...) -> None: ...

class CreateProductBulkRequest(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

class UpdateProductRequest(_message.Message):
    __slots__ = ("product",)
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    product: Product
    def __init__(self, product: _Optional[_Union[Product, _Mapping]] = ...) -> None: ...

class UpdateProductBulkRequest(_message.Message):
    __slots__ = ("products",)
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...

class DeleteProductRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteProductBulkRequest(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ProductResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class ProcessedProductRequest(_message.Message):
    __slots__ = ("product", "operation")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    product: Product
    operation: str
    def __init__(self, product: _Optional[_Union[Product, _Mapping]] = ..., operation: _Optional[str] = ...) -> None: ...

class ProcessedProductResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
