package com.hl.pmp.domain

import kotlinx.coroutines.reactor.awaitSingle
import org.springframework.stereotype.Service

@Service
class ProductService(
    val productRepository: ProductRepository,
    val productBulkRepository: ProductBulkRepository,
) {
    suspend fun create(product: Product): Product = productRepository.save(product).awaitSingle()

    suspend fun createBulk(products: List<Product>) = productBulkRepository.bulkCreate(products)

    suspend fun update(product: Product): Product = productRepository.save(product).awaitSingle()

    suspend fun updateBulk(products: List<Product>) = productBulkRepository.bulkModify(products)

    suspend fun delete(id: String) = productRepository.deleteById(id).awaitSingle()

    suspend fun deleteBulk(ids: List<String>) = productBulkRepository.bulkRemove(ids)
}
