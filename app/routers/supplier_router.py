from fastapi import APIRouter
from app.schemas.supplier_schema import SupplierBase
from app.services.supplier_service import (
    create_supplier_service,
    get_suppliers_service
)  

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

@router.get("")
def get_suppliers():
    return get_suppliers_service()

@router.post("/add")
def create_supplier(supplier: SupplierBase):
    return create_supplier_service(supplier)