package com.hl.pmp.domain

import org.springframework.data.annotation.CreatedDate
import org.springframework.data.annotation.Id
import org.springframework.data.annotation.LastModifiedDate
import org.springframework.data.mongodb.core.mapping.Document
import java.time.LocalDateTime

@Document(collection = "products")
class Product private constructor(
    @Id
    val id: String,
    val name: String,
    val price: Int,
    @CreatedDate
    val createdAt: LocalDateTime,
    @LastModifiedDate
    val updatedAt: LocalDateTime,
) {
    companion object {
        operator fun invoke(
            name: String,
            price: Int,
        ): Product {
            require(name.isNotBlank()) { "Name must not be blank" }
            require(price > 0) { "Price must be greater than 0" }

            val now = LocalDateTime.now()
            return Product(
                id = "",
                name = name,
                price = price,
                createdAt = now,
                updatedAt = now,
            )
        }
    }
}
