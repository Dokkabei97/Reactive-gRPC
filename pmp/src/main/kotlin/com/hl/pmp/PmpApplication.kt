package com.hl.pmp

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import reactor.blockhound.BlockHound

@SpringBootApplication
class PmpApplication

fun main(args: Array<String>) {
    BlockHound.install()
    runApplication<PmpApplication>(*args)
}
