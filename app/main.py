from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Inventory Management API!"}

@app.get("/products")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop", "quantity": 10, "price": 999.99},
            {"id": 2, "name": "Mouse", "quantity": 50, "price": 29.99}
        ]
    }

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