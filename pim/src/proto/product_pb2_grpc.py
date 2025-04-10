# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import src.proto.product_pb2 as product__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in product_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProduct = channel.unary_unary(
                '/product.ProductService/CreateProduct',
                request_serializer=product__pb2.CreateProductRequest.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                _registered_method=True)
        self.UpdateProduct = channel.unary_unary(
                '/product.ProductService/UpdateProduct',
                request_serializer=product__pb2.UpdateProductRequest.SerializeToString,
                response_deserializer=product__pb2.ProductResponse.FromString,
                _registered_method=True)
        self.DeleteProduct = channel.unary_unary(
                '/product.ProductService/DeleteProduct',
                request_serializer=product__pb2.DeleteProductRequest.SerializeToString,
                response_deserializer=product__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.SendProcessedProduct = channel.unary_unary(
                '/product.ProductService/SendProcessedProduct',
                request_serializer=product__pb2.ProcessedProductRequest.SerializeToString,
                response_deserializer=product__pb2.ProcessedProductResponse.FromString,
                _registered_method=True)
        self.ResendProcessedProduct = channel.unary_unary(
                '/product.ProductService/ResendProcessedProduct',
                request_serializer=product__pb2.ProcessedProductRequest.SerializeToString,
                response_deserializer=product__pb2.ProcessedProductResponse.FromString,
                _registered_method=True)


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateProduct(self, request, context):
        """PIM -> PMP 상품 생성
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProduct(self, request, context):
        """PIM -> PMP 상품 업데이트
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProduct(self, request, context):
        """PIM -> PMP 상품 삭제
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendProcessedProduct(self, request, context):
        """PMP -> POC 로 처리된 상품 정보 전송
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResendProcessedProduct(self, request, context):
        """POC -> PIM 전달 받은 상품 정보 재전송
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=product__pb2.CreateProductRequest.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'UpdateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProduct,
                    request_deserializer=product__pb2.UpdateProductRequest.FromString,
                    response_serializer=product__pb2.ProductResponse.SerializeToString,
            ),
            'DeleteProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProduct,
                    request_deserializer=product__pb2.DeleteProductRequest.FromString,
                    response_serializer=product__pb2.DeleteResponse.SerializeToString,
            ),
            'SendProcessedProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.SendProcessedProduct,
                    request_deserializer=product__pb2.ProcessedProductRequest.FromString,
                    response_serializer=product__pb2.ProcessedProductResponse.SerializeToString,
            ),
            'ResendProcessedProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.ResendProcessedProduct,
                    request_deserializer=product__pb2.ProcessedProductRequest.FromString,
                    response_serializer=product__pb2.ProcessedProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'product.ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('product.ProductService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/product.ProductService/CreateProduct',
            product__pb2.CreateProductRequest.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/product.ProductService/UpdateProduct',
            product__pb2.UpdateProductRequest.SerializeToString,
            product__pb2.ProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/product.ProductService/DeleteProduct',
            product__pb2.DeleteProductRequest.SerializeToString,
            product__pb2.DeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SendProcessedProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/product.ProductService/SendProcessedProduct',
            product__pb2.ProcessedProductRequest.SerializeToString,
            product__pb2.ProcessedProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ResendProcessedProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/product.ProductService/ResendProcessedProduct',
            product__pb2.ProcessedProductRequest.SerializeToString,
            product__pb2.ProcessedProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
