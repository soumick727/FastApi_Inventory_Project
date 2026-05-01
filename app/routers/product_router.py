from fastapi import APIRouter
from app.schemas.product_schema import ProductBase

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop", "quantity": 10, "price": 999.99},
            {"id": 2, "name": "Mouse", "quantity": 50, "price": 29.99}
        ]
    }

@router.get("/search")
def search_product(name: str):
    return {
        "message": "Search Result",
        "search_keyword": name
    }

@router.get("/{product_id}")
def get_single_product(product_id: int):
    return{
        "product_id": product_id,
        "name": "Sample Product",
        "quantity": 20,
        "price": 49.99
    }

@router.post("/add")
def create_product(product: ProductBase):
    return {
        "message": "Product created successfully!",
        "product_name": product.name,
        "product_quantity": product.quantity,
        "product_price": product.price
    }