from dataclasses import dataclass


@dataclass
class Product:
    id: str
    name: str
    price: int    
    created_at: str
    updated_at: str