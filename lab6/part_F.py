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

print(products)
print(in_stock)
print(unique_categories)