import grpc
from src.proto import product_pb2, product_pb2_grpc
from src.domain.product import Product

class ProductGrpcClient:
    def __init__(self, target="localhost:50051"):
        self.target = target
        self.channel = None
        self.stub = None
    
    async def connect(self):
        self.channel = grpc.aio.insecure_channel(self.target)
        self.stub = product_pb2_grpc.ProductServiceStub(self.channel)
    
    async def close(self):
        if self.channel:
            await self.channel.close()
    
    def _to_proto_product(self, product: Product) -> product_pb2.Product:
        return product_pb2.Product(
            id=product.id,
            name=product.name,
            price=product.price,
            stock=product.stock,
            category=product.category,
            created_at=product.created_at,
            updated_at=product.updated_at
        )
    
    async def create_product(self, product: Product):
        if not self.stub:
            await self.connect()
        
        proto_product = self._to_proto_product(product)
        request = product_pb2.CreateProductRequest(product=proto_product)
        
        response = await self.stub.CreateProduct(request)
        return response
    
    async def update_product(self, product: Product):
        if not self.stub:
            await self.connect()
        
        proto_product = self._to_proto_product(product)
        request = product_pb2.UpdateProductRequest(product=proto_product)
        
        response = await self.stub.UpdateProduct(request)
        return response
    
    async def delete_product(self, product_id: str):
        if not self.stub:
            await self.connect()
        
        request = product_pb2.DeleteProductRequest(id=product_id)
        
        response = await self.stub.DeleteProduct(request)
        return response
