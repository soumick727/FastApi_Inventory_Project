def get_suppliers_service():
    return {
        "suppliers": [
            {"id": 1, "name": "Tech Supplies Co.", "contact": "123-456-7890"},
            {"id": 2, "name": "Gadget World", "contact": "987-654-3210"}
        ]
    }

def create_supplier_service(supplier):
    return {
        "message": "Supplier created successfully!",
        "supplier_name": supplier.name,
        "supplier_phone": supplier.phone,
        "supplier_address": supplier.address
    }