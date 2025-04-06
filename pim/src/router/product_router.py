from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from src.infra.grpc_client import ProductGrpcClient
from src.domain.product import Product

router = APIRouter(
    prefix="/products",
)


# Pydantic 모델 정의
class ProductRequest(BaseModel):
    id: Optional[str] = None
    name: str
    price: int
    stock: int
    category: str


# gRPC 클라이언트 의존성
async def get_grpc_client():
    client = ProductGrpcClient()
    await client.connect()
    try:
        yield client
    finally:
        await client.close()


@router.post("")
async def create_product(product_req: ProductRequest, grpc_client: ProductGrpcClient = Depends(get_grpc_client)):
    now = datetime.now().isoformat()
    product = Product(
        id=product_req.id or str(hash(now)),
        name=product_req.name,
        price=product_req.price,
        stock=product_req.stock,
        category=product_req.category,
        created_at=now,
        updated_at=now
    )

    try:
        response = await grpc_client.create_product(product)
        return {"message": "Product created", "success": response.success, "details": response.message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create product: {str(e)}")


@router.put("/{product_id}")
async def update_product(product_id: str, product_req: ProductRequest,
                         grpc_client: ProductGrpcClient = Depends(get_grpc_client)):
    now = datetime.now().isoformat()
    product = Product(
        id=product_id,
        name=product_req.name,
        price=product_req.price,
        stock=product_req.stock,
        category=product_req.category,
        created_at="",  # 서버에서 처리
        updated_at=now
    )

    try:
        response = await grpc_client.update_product(product)
        return {"message": "Product updated", "success": response.success, "details": response.message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update product: {str(e)}")


@router.delete("/{product_id}")
async def delete_product(product_id: str, grpc_client: ProductGrpcClient = Depends(get_grpc_client)):
    try:
        response = await grpc_client.delete_product(product_id)
        return {"message": "Product deleted", "success": response.success, "details": response.message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete product: {str(e)}")
