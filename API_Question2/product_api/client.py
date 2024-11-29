import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/products/"

# Add a new product
def add_product(name, description, price):
    product_data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, data=json.dumps(product_data), headers={"Content-Type": "application/json"})
    if response.status_code == 201:
        print("Product added successfully:", response.json())
    else:
        print("Failed to add product:", response.status_code, response.json())

# Get list of products
def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        products = response.json()
        print("Products list:", products)
    else:
        print("Failed to fetch products:", response.status_code)

if __name__ == "__main__":
    # Example usage
    add_product("Product 1", "A great product", 29.99)
    get_products()
