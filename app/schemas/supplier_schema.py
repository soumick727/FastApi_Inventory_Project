from pydantic import BaseModel

class SupplierBase(BaseModel):
    name: str
    phone: str
    address: str 