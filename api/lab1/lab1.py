from api_client import get_json
import requests

products = get_json("https://fakestoreapi.com/products")
for product in products:
    print(product)

sorted_products = sorted(products, key=lambda p: p["price"])
for product in sorted_products:
    print(f"{product['title']}, {product['price']}")

"""
categories = get_json("https://fakestoreapi.com/products/categories")
choice = None
while choice not in categories:
    print(categories)
    choice = input("Choose a category from the above options: ")

category_products = categories = get_json(f"https://fakestoreapi.com/products/category/{choice}")
print(f"The category {choice} has {len(category_products)} products")
sorted_category_products = sorted(category_products, key=lambda p: p["price"])
cheapest_product = sorted_category_products[0]
print(f"The cheapest product in {choice} is {cheapest_product['title']} with price {cheapest_product['price']}")
"""

new_product = {
    "title": "Silver owl signet ring",
    "description": "A sterling silver signet ring engraved with a motif of an owl",
    "price": 150,
    "image": "https://thumbs.dreamstime.com/b/silver-signet-ring-featuring-detailed-owl-carving-rests-dark-textured-surface-circular-design-polished-finish-351125338.jpg?w=768",
    "category": "jewelery",
}
response = requests.post("https://fakestoreapi.com/products", json=new_product, timeout=5)
print(response.status_code)
print(response)
print(response.json())

response = requests.patch("http://fakestoreapi.com/products/7", json={"price": 199}, timeout=5)
print(response.status_code)
print(response)
print(response.json())


get_json("https://fakestoreapi.com/wrong-url")
get_json("https://this-domain-does-not-exist-hopefully.com")
get_json("https://fakestoreapi.com/products", timeout=0.001)