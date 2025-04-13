package com.hl.pmp.domain

import io.grpc.stub.StreamObserver
import org.springframework.grpc.product.proto.*
import org.springframework.grpc.server.service.GrpcService

@GrpcService
class GrpcServerService(
    val productService: ProductService,
) : ProductServiceGrpc.ProductServiceImplBase() {
    override fun createProduct(
        request: CreateProductRequest?,
        responseObserver: StreamObserver<ProductResponse>?,
    ) {
        super.createProduct(request, responseObserver)
    }

    override fun createProductsBulk(
        request: CreateProductBulkRequest?,
        responseObserver: StreamObserver<ProductResponse>?,
    ) {
        super.createProductsBulk(request, responseObserver)
    }

    override fun updateProduct(
        request: UpdateProductRequest?,
        responseObserver: StreamObserver<ProductResponse>?,
    ) {
        super.updateProduct(request, responseObserver)
    }

    override fun updateProductsBulk(
        request: UpdateProductBulkRequest?,
        responseObserver: StreamObserver<ProductResponse>?,
    ) {
        super.updateProductsBulk(request, responseObserver)
    }

    override fun deleteProduct(
        request: DeleteProductRequest?,
        responseObserver: StreamObserver<ProductResponse>?,
    ) {
        super.deleteProduct(request, responseObserver)
    }

    override fun deleteProductsBulk(
        request: DeleteProductBulkRequest?,
        responseObserver: StreamObserver<ProductResponse>?,
    ) {
        super.deleteProductsBulk(request, responseObserver)
    }
}
