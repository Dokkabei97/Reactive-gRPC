from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    price: int
    stock: int
    category: str
    created_at: str
    updated_at: str