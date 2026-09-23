raw_data = [
    {"name": "MILK", "category": "dairy", "price": 15, "stock": 25},
    {"name": "yoghurt   ", "category": "DaiRY", "price": 20, "stock": 20},
    {"name": " eggS", "category": " dairy ", "price": 40, "stock": 10},
    {"name": "CARROTS ", "category": "VEGETABLES", "price": 15, "stock": 13},
    {"name": "  cabBage ", "category": "vegetables ", "price": 10, "stock": 20},
    {"name": "Onion ", "category": "Vegetables  ", "price": 5, "stock": 30},
    {"name": " Pomegranate  ", "category": "Fruit", "price": 20, "stock": 10},
    {"name": "ORANGE", "category": "FRUIT", "price": 10, "stock": 0},
    {"name": "Banana  ", "category": "fruit ", "price": 7, "stock": 30},
    {"name": "appLE", "category": "FRuit ", "price": 7, "stock": 40},
    {"name": "PEAR", "category": " FRUIT", "price": 10, "stock": 23},
    {"name": "KIWI ", "category": " fruit   ", "price": 10, "stock": 14},
    {"name": "tomato", "category": "vegetables", "price": 10, "stock": 0},
]

products = [
    {
        "name": product.get("name", "").strip().title(),
        "category": product.get("category", "").strip().title(),
        "price": product.get("price", 0),
        "stock": product.get("stock", 0)
    } 
    for product in raw_data]

in_stock = [product for product in products if product.get("stock") > 0]
unique_categories = {product.get("category") for product in products}

products_inventory_values = [
    {
        product.get("name", ""): product.get("price", 0) *product.get("stock", 0),
    } 
    for product in products]

sorted_products_inventory_values = sorted(products_inventory_values, 
                                          key=lambda product: next(iter(product.values())), 
                                          reverse=True)

# Two comprehensions for getting all vegetables.
# The first one is clearer because it has descriptive naming, does not create a list unnecessarily,
# and it actually checks the category key-value pair precisely. 
# The second one would return any items that has "Vegetables" anywhere in its values.
vegetables = [product for product in products if product.get("category") == "Vegetables"]
vegetables_complicated = [x for x in products if "Vegetables" in list(x.values())]

vegetable_names = [product["name"] for product in products if product.get("category") == "Vegetables"]
vegetable_stock = [product["stock"] for product in products if product.get("category") == "Vegetables"]
zipped_vegetables = zip(vegetable_names, vegetable_stock)


print(products)
print(in_stock)
print(unique_categories)
print(products_inventory_values)
print(sorted_products_inventory_values)

for rank, product in enumerate(sorted_products_inventory_values, start=1):
    name, value = next(iter(product.items()))
    print(f"{rank}. {name}, {value} kr")

for value in zipped_vegetables:
    print(value)

print("Vegetables", vegetables)
print("Vegetables", vegetables_complicated)