from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Python Inventory API")

class Product(BaseModel):
    id: int
    name: str

products = [
    {"id": 101, "name": "Laptop"}
]

@app.get("/health")
def health():
    return {
        "status": "UP",
        "app": "Python Inventory API"
    }

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def add_product(product: Product):
    products.append(product.dict())
    return product