package com.hl.pmp.utils

import com.mongodb.bulk.BulkWriteResult
import kotlinx.coroutines.reactor.awaitSingle
import org.springframework.data.mongodb.core.BulkOperations
import org.springframework.data.mongodb.core.ReactiveMongoTemplate
import org.springframework.data.mongodb.core.query.Query
import org.springframework.data.mongodb.core.query.Update

abstract class MongoCustomRepositorySupport<T>(
    protected val document: Class<T>,
    protected val mongoTemplate: ReactiveMongoTemplate,
) {
    protected suspend fun <T : Any> bulkInsert(
        documents: List<T>,
        bulkMode: BulkOperations.BulkMode,
    ): BulkWriteResult {
        val bulkOps = mongoTemplate.bulkOps(bulkMode, document)
        documents.forEach { bulkOps.insert(it) }
        return bulkOps.execute().awaitSingle()
    }

    protected suspend fun bulkUpdate(
        operations: List<Pair<() -> Query, () -> Update>>,
        bulkMode: BulkOperations.BulkMode,
    ): BulkWriteResult {
        val bulkOps = mongoTemplate.bulkOps(bulkMode, document)
        operations.forEach { (queryCreator, updateCreator) ->
            bulkOps.updateOne(queryCreator.invoke(), updateCreator.invoke())
        }
        return bulkOps.execute().awaitSingle()
    }

    protected suspend fun bulkDelete(
        operations: List<() -> Query>,
        bulkMode: BulkOperations.BulkMode,
    ): BulkWriteResult {
        val bulkOps = mongoTemplate.bulkOps(bulkMode, document)
        operations.forEach {
            bulkOps.remove(it.invoke())
        }
        return bulkOps.execute().awaitSingle()
    }
}
