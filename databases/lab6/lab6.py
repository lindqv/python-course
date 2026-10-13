from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client["webshop"]

for product in db.products.find({"category": "Accessories"}):
    pprint(product)

for customer in db.customers.find({"city": "Göteborg"}):
    print(customer.get("first_name"), customer.get("last_name"))

for product in db.products.find():
    print(product.get("name"), product.get("price"))

print(db.customers.count_documents({"city": "Uppsala"}))

sandals = db.products.find_one({"name": "Sandals"})
print(sandals.get("stock"))

for customers in db.customers.find({"newsletter": True}):
    print(customers.get("first_name"))

result = db.customers.insert_one({
    "first_name": "Sanne",
    "last_name": "Lindqvist",
    "email": "s.lindqvist@example.com",
    "city": "Stockholm"
    })

pprint(db.customers.find_one({"_id": result.inserted_id}))

db.products.insert_many([
    {
        "_id": 13,
        "name": "Knit sweater", 
        "category": "Clothing",
        "price": 399,
        "stock": 15,
        "tags": ["winter"],
        "details": {"color": "grey", "material": "cotton"},
    }, 
    {
        "_id": 14,
        "name": "Corduroy trousers", 
        "category": "Clothing",
        "price": 499,
        "stock": 10,
        "tags": ["winter"],
        "details": {"color": "green", "material": "cotton"},
    }
])

print(db.products.count_documents({}))

for customer in db.customers.find():
    print(f"{customer.get('first_name')} {customer.get('last_name')} ({customer.get('city')})")

for order in db.orders.find():
    order_items = order.get("items", [])
    order_items_count = sum(item.get("quantity", 0) for item in order_items)
    print(f"Order {order.get('_id')}: {order_items_count} items")
