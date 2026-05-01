from fastapi import FastAPI
from app.routers import product_router
from app.schemas.supplier_schema import SupplierBase
from app.schemas.category_schema import CategoryBase

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Inventory Management API!"}


@app.get("/suppliers")
def get_suppliers():
    return {
        "suppliers": [
            {"id": 1, "name": "Tech Supplies Co.", "contact": "123-456-7890"},
            {"id": 2, "name": "Gadget World", "contact": "987-654-3210"}
        ]
    }
    
@app.get("/categories")
def get_categories():
    return {
        "categories": [
            {"id": 1, "name": "Electronics"},
            {"id": 2, "name": "Grocery"},
            {"id": 3, "name": "Clothing"}
        ]
    }

@app.get("/dashboard")
def get_dashboard():
    return {
        "total_products": 100,
        "total_low_stock": 5,
        "total_out_of_stock": 2,
    }


    
@app.post("/suppliers/add")
def create_supplier(supplier: SupplierBase):
    return {
        "message": "Supplier created successfully!",
        "supplier_name": supplier.name,
        "supplier_phone": supplier.phone,
        "supplier_address": supplier.address
    }

@app.post("/categories/add")
def create_category(category: CategoryBase):
    return {
        "message": "Category created successfully!",
        "category_title": category.title
    }
    
app.include_router(product_router.router)