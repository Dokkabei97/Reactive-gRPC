from src.domain.product import Product


def make_dummy_product():
    return Product(
        id="1",
        name="Test Product",
        price=1000,
        created_at="2025-04-13T00:00:00Z",
        updated_at="2025-04-13T00:00:00Z",
    )


def make_dummy_product_list(count: int):
    return [
        Product(
            id=str(i),
            name=f"Test Product {i}",
            price=1000 + i,
            created_at="2025-04-13T00:00:00Z",
            updated_at="2025-04-13T00:00:00Z",
        )
        for i in range(count)
    ]


def update_dummy_product():
    return Product(
        id="1",
        name="Updated Product",
        price=2000,
        created_at="2025-04-13T00:00:00Z",
        updated_at="2025-04-13T11:00:00Z",
    )


def update_dummy_product_list(count: int):
    return [
        Product(
            id=str(i),
            name=f"Updated Product {i}",
            price=2000 + i,
            created_at="2025-04-13T00:00:00Z",
            updated_at="2025-04-13T11:00:00Z",
        )
        for i in range(count)
    ]


def delete_dummy_product():
    return 1


def delete_dummy_product_list(count: int):
    return [i for i in range(count)]
