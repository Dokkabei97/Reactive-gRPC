import asyncio
import functools

import grpc.aio
from fastapi import FastAPI

from src.router import product_router
from src.domain.product_service_impl import ProductServiceImpl
from src.proto import product_pb2_grpc

# FastAPI 앱
app = FastAPI()
app.include_router(product_router.router)


# FastAPI와 gRPC 서버 동시 실행
def async_run(func):
    @functools.wraps(func)
    # gRPC 서버를 백그라운드 태스크로 실행
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper


# gRPC 서버
@async_run
async def serve_grpc():
    server = grpc.aio.server()
    product_pb2_grpc.add_ProductServiceServicer_to_server(
        ProductServiceImpl(), server
    )
    listen_addr = "[::]:50052"  # 포트 번호는 필요에 따라 조정
    server.add_insecure_port(listen_addr)
    print(f"gRPC server starting on {listen_addr}")
    await server.start()
    await server.wait_for_termination()
