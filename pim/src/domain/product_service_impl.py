from src.proto.product_pb2_grpc import ProductServiceServicer
from src.proto.product_pb2 import ProcessedProductResponse
from src.domain.product import Product

class ProductServiceImpl(ProductServiceServicer):
    async def ResendProcessedProduct(self, request, context):
        try:
            print(f"Received processed product: {request.product.id}, Operation: {request.operation}")
            
            # 여기에 비즈니스 로직 추가
            # 예: DB에 저장하거나 다른 처리를 수행
            
            # 요청에서 Product 객체 추출
            product_proto = request.product
            product = Product(
                id=product_proto.id,
                name=product_proto.name,
                price=product_proto.price,
                stock=product_proto.stock,
                category=product_proto.category,
                created_at=product_proto.created_at,
                updated_at=product_proto.updated_at
            )
            
            # 처리 로직 추가...
            
            return ProcessedProductResponse(
                success=True,
                message=f"Product {request.product.id} successfully processed"
            )
        except Exception as e:
            return ProcessedProductResponse(
                success=False,
                message=f"Failed to process product: {str(e)}"
            )
