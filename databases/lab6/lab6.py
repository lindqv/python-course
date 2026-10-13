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
