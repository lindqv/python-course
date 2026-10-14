from pymongo import MongoClient
from datetime import datetime
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


for product in db.products.find({"category": "Accessories"}):
    print(product)

db.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}})

for product in db.products.find({"category": "Accessories"}):
    print(product)


print(db.products.find_one({"name": "Rain Jacket"}))
db.products.update_one({"name": "Rain Jacket"}, {"$push": {"tags": "new"}})
db.products.update_one({"name": "Rain Jacket"}, {"$set": {"restock_date": datetime.now()}})
print(db.products.find_one({"name": "Rain Jacket"}))


orders = db.orders.find({"status" : "new", "order_date": {"$lt": datetime(2026, 3, 20)}})
for order in orders:
    print(order)
print("Order count before", 
      db.orders.count_documents({"status" : "new", "order_date": {"$lt": datetime(2026, 3, 20)}}))

result = db.orders.delete_many({"status" : "new", "order_date": {"$lt": datetime(2026, 3, 20)}})
print("Deleted count", result.deleted_count)

orders = db.orders.find({"status" : "new", "order_date": {"$lt": datetime(2026, 3, 20)}})
for order in orders:
    print(order)
print("Order count after", 
      db.orders.count_documents({"status" : "new", "order_date": {"$lt": datetime(2026, 3, 20)}}))