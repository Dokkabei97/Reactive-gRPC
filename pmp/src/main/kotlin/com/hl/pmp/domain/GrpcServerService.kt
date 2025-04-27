package com.hl.pmp.domain

import org.springframework.grpc.product.proto.CreateProductBulkRequest
import org.springframework.grpc.product.proto.CreateProductRequest
import org.springframework.grpc.product.proto.DeleteProductBulkRequest
import org.springframework.grpc.product.proto.DeleteProductRequest
import org.springframework.grpc.product.proto.ProductResponse
import org.springframework.grpc.product.proto.ProductServiceGrpcKt
import org.springframework.grpc.product.proto.UpdateProductBulkRequest
import org.springframework.grpc.product.proto.UpdateProductRequest
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

    override suspend fun createProductsBulk(request: CreateProductBulkRequest): ProductResponse {
        val products =
            request.productsList.map {
                Product(
                    it.name,
                    it.price,
                )
            }
        productService.createBulk(products)

        return ProductResponse
            .newBuilder()
            .setMessage("Products created")
            .build()
    }

    override suspend fun updateProduct(request: UpdateProductRequest): ProductResponse {
        val product =
            Product(
                request.product.name,
                request.product.price,
            )
        productService.update(product)

        return ProductResponse
            .newBuilder()
            .setMessage("Product updated")
            .build()
    }

    override suspend fun updateProductsBulk(request: UpdateProductBulkRequest): ProductResponse = super.updateProductsBulk(request)

    override suspend fun deleteProduct(request: DeleteProductRequest): ProductResponse = super.deleteProduct(request)

    override suspend fun deleteProductsBulk(request: DeleteProductBulkRequest): ProductResponse = super.deleteProductsBulk(request)
}
