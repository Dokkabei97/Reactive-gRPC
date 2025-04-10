# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: product.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'product.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproduct.proto\x12\x07product\"M\n\x0eProductRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x12\x0c\n\x04page\x18\x03 \x01(\x05\x12\x0c\n\x04size\x18\x04 \x01(\x05\"\x81\x01\n\x0fProductResponse\x12\"\n\x08products\x18\x01 \x03(\x0b\x32\x10.product.Product\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x12\x13\n\x0btotal_pages\x18\x03 \x01(\x05\x12\x0f\n\x07success\x18\x04 \x01(\x08\x12\x0f\n\x07message\x18\x05 \x01(\t\"{\n\x07Product\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x05\x12\r\n\x05stock\x18\x04 \x01(\x05\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\t\x12\x12\n\ncreated_at\x18\x06 \x01(\t\x12\x12\n\nupdated_at\x18\x07 \x01(\t\"9\n\x14\x43reateProductRequest\x12!\n\x07product\x18\x01 \x01(\x0b\x32\x10.product.Product\"9\n\x14UpdateProductRequest\x12!\n\x07product\x18\x01 \x01(\x0b\x32\x10.product.Product\"\"\n\x14\x44\x65leteProductRequest\x12\n\n\x02id\x18\x01 \x01(\t\"2\n\x0e\x44\x65leteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"O\n\x17ProcessedProductRequest\x12!\n\x07product\x18\x01 \x01(\x0b\x32\x10.product.Product\x12\x11\n\toperation\x18\x02 \x01(\t\"<\n\x18ProcessedProductResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xa9\x03\n\x0eProductService\x12H\n\rCreateProduct\x12\x1d.product.CreateProductRequest\x1a\x18.product.ProductResponse\x12H\n\rUpdateProduct\x12\x1d.product.UpdateProductRequest\x1a\x18.product.ProductResponse\x12G\n\rDeleteProduct\x12\x1d.product.DeleteProductRequest\x1a\x17.product.DeleteResponse\x12[\n\x14SendProcessedProduct\x12 .product.ProcessedProductRequest\x1a!.product.ProcessedProductResponse\x12]\n\x16ResendProcessedProduct\x12 .product.ProcessedProductRequest\x1a!.product.ProcessedProductResponseBA\n&org.springframework.grpc.product.protoB\x0cProductProtoP\x01Z\x07./protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&org.springframework.grpc.product.protoB\014ProductProtoP\001Z\007./proto'
  _globals['_PRODUCTREQUEST']._serialized_start=26
  _globals['_PRODUCTREQUEST']._serialized_end=103
  _globals['_PRODUCTRESPONSE']._serialized_start=106
  _globals['_PRODUCTRESPONSE']._serialized_end=235
  _globals['_PRODUCT']._serialized_start=237
  _globals['_PRODUCT']._serialized_end=360
  _globals['_CREATEPRODUCTREQUEST']._serialized_start=362
  _globals['_CREATEPRODUCTREQUEST']._serialized_end=419
  _globals['_UPDATEPRODUCTREQUEST']._serialized_start=421
  _globals['_UPDATEPRODUCTREQUEST']._serialized_end=478
  _globals['_DELETEPRODUCTREQUEST']._serialized_start=480
  _globals['_DELETEPRODUCTREQUEST']._serialized_end=514
  _globals['_DELETERESPONSE']._serialized_start=516
  _globals['_DELETERESPONSE']._serialized_end=566
  _globals['_PROCESSEDPRODUCTREQUEST']._serialized_start=568
  _globals['_PROCESSEDPRODUCTREQUEST']._serialized_end=647
  _globals['_PROCESSEDPRODUCTRESPONSE']._serialized_start=649
  _globals['_PROCESSEDPRODUCTRESPONSE']._serialized_end=709
  _globals['_PRODUCTSERVICE']._serialized_start=712
  _globals['_PRODUCTSERVICE']._serialized_end=1137
# @@protoc_insertion_point(module_scope)
