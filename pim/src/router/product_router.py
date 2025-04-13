from fastapi import APIRouter, Depends

from src.infra.grpc_client import ProductGrpcClient
from src.utils.dummy_product_maker import *

router = APIRouter(
    prefix="/products",
)


# gRPC 클라이언트 의존성
async def get_grpc_client():
    client = ProductGrpcClient()
    await client.connect()
    try:
        yield client
    finally:
        await client.close()


@router.post
async def create_product(
        client: ProductGrpcClient = Depends(get_grpc_client),
):
    await client.create_product(make_dummy_product())

@router.post("/bulk")
async def create_product_bulk(
        count: int = 1000,
        client: ProductGrpcClient = Depends(get_grpc_client),
):
    await client.create_product_bulk(make_dummy_product_list(count))


@router.put
async def update_product(
        client: ProductGrpcClient = Depends(get_grpc_client),
):
    await client.update_product(update_dummy_product())

@router.put("/bulk")
async def update_product_bulk(
        count: int = 1000,
        client: ProductGrpcClient = Depends(get_grpc_client),
):
    await client.update_product_bulk(update_dummy_product_list(count))

@router.delete
async def delete_product(
        client: ProductGrpcClient = Depends(get_grpc_client),
):
    await client.delete_product(delete_dummy_product())

@router.delete("/bulk")
async def delete_product_bulk(
        count: int = 1000,
        client: ProductGrpcClient = Depends(get_grpc_client),
):
    await client.delete_product_bulk(delete_dummy_product_list(count))