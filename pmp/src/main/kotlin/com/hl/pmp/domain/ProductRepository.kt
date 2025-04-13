package com.hl.pmp.domain

import org.springframework.data.mongodb.repository.ReactiveMongoRepository
import org.springframework.stereotype.Repository

@Repository
interface ProductRepository : ReactiveMongoRepository<Product, String>
