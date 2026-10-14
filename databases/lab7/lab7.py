from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for product in db.products.find({"price": {"$gt": 1000}}):
    print(product["name"], product["price"])

for order in db.orders.find({"status": {"$ne": "delivered"}}):
    print(order["_id"], order["status"])

for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
    print(customer["first_name"])

for product in db.products.find({"details.color": "white"}):
    print(product["name"])

for product in db.products.find({"tags": "sport"}):
    print(product["name"])

for product in db.products.find().sort("price").limit(5):
    print(product["name"], product["price"])

for order in db.orders.find({"items.product_id": 2}):
    print("Order with id", order["_id"], "has product with id 2")