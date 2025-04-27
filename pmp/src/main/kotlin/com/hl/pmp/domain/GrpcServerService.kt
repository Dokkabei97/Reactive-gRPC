package com.hl.pmp.domain

import org.springframework.grpc.product.proto.CreateProductRequest
import org.springframework.grpc.product.proto.ProductResponse
import org.springframework.grpc.product.proto.ProductServiceGrpcKt
import org.springframework.stereotype.Service

@Service
class GrpcServerService(
    val productService: ProductService,
) : ProductServiceGrpcKt.ProductServiceCoroutineImplBase() {
    override suspend fun createProduct(request: CreateProductRequest): ProductResponse {
        val product =
            Product(
                request.product.name,
                request.product.price,
            )
        productService.create(product)

        return ProductResponse
            .newBuilder()
            .setMessage("Product created")
            .build()
    }
}
