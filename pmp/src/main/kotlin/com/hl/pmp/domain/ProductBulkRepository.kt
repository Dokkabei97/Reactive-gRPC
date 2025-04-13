package com.hl.pmp.domain

import com.hl.pmp.utils.MongoCustomRepositorySupport
import org.springframework.data.mongodb.core.BulkOperations
import org.springframework.data.mongodb.core.ReactiveMongoTemplate
import org.springframework.data.mongodb.core.query.Criteria
import org.springframework.data.mongodb.core.query.Query
import org.springframework.data.mongodb.core.query.Update
import org.springframework.stereotype.Component

@Component
class ProductBulkRepository(
    mongoTemplate: ReactiveMongoTemplate,
) : MongoCustomRepositorySupport<Product>(Product::class.java, mongoTemplate) {
    suspend fun bulkCreate(products: List<Product>) {
        bulkInsert(
            products,
            BulkOperations.BulkMode.UNORDERED,
        )
    }

    suspend fun bulkModify(products: List<Product>) {
        bulkUpdate(
            products.map { product ->
                {
                    Query.query(
                        Criteria.where("id").`is`(product.id),
                    )
                } to {
                    Update()
                        .set("name", product.name)
                        .set("price", product.price)
                }
            },
            BulkOperations.BulkMode.UNORDERED,
        )
    }

    suspend fun bulkRemove(ids: List<String>) {
        bulkDelete(
            ids.map { id ->
                {
                    Query.query(
                        Criteria.where("id").`is`(id),
                    )
                }
            },
            BulkOperations.BulkMode.UNORDERED,
        )
    }
}
