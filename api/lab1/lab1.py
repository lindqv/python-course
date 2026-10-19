from api_client import get_json

products = get_json("https://fakestoreapi.com/products")
for product in products:
    print(product)

sorted_products = sorted(products, key=lambda p: p["price"])
for product in sorted_products:
    print(f"{product['title']}, {product['price']}")


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