from contextlib import asynccontextmanager

import grpc.aio
from fastapi import FastAPI

from src.router import product_router


async def serve_grpc():
    server = grpc.aio.server()

    listen_addr = "[::]:50052"  # 포트 번호는 필요에 따라 조정
    server.add_insecure_port(listen_addr)
    await server.start()
    print(f"gRPC server starting on {listen_addr}")
    await server.wait_for_termination()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # gRPC 서버를 비동기로 실행
    import asyncio
    loop = asyncio.get_event_loop()
    grpc_server_task = loop.create_task(serve_grpc())

    yield  # FastAPI 앱이 실행되는 동안 대기

    # FastAPI 앱 종료 시 gRPC 서버 종료
    grpc_server_task.cancel()
    try:
        await grpc_server_task
    except asyncio.CancelledError:
        pass


# FastAPI 앱
app = FastAPI(
    # lifespan=lifespan
)
app.include_router(product_router.router)
