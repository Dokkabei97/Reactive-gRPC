package com.hl.pmp

import io.grpc.Status
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean
import org.springframework.grpc.server.exception.GrpcExceptionHandler
import reactor.blockhound.BlockHound

@SpringBootApplication
class PmpApplication {
    @Bean
    fun grpcExceptionHandler(): GrpcExceptionHandler =
        GrpcExceptionHandler { ex ->
            if (ex is IllegalArgumentException) {
                Status.INVALID_ARGUMENT.withDescription(ex.message)
            } else {
                Status.INTERNAL
                    .withCause(ex)
                    .withDescription(ex.message)
            }
        }
}

fun main(args: Array<String>) {
    BlockHound.install()
    runApplication<PmpApplication>(*args)
}
