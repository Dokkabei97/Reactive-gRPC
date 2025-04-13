package com.hl.pmp.config

import org.springframework.context.annotation.Configuration
import org.springframework.data.mongodb.config.AbstractReactiveMongoConfiguration
import org.springframework.data.mongodb.config.EnableReactiveMongoAuditing
import org.springframework.data.mongodb.repository.config.EnableReactiveMongoRepositories

@Configuration
@EnableReactiveMongoAuditing
@EnableReactiveMongoRepositories
class MongoConfig : AbstractReactiveMongoConfiguration() {
    override fun getDatabaseName(): String = "pmp"

    override fun getMappingBasePackages(): MutableCollection<String> =
        mutableListOf(
            "com.hl.pmp.domain",
        )
}
