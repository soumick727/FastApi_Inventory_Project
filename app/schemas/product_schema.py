from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    quantity: int
    price: float