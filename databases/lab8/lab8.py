from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# Exercise 3
db.drop_collection("newsletter_signups")
db.create_collection("newsletter_signups", validator={"$jsonSchema": {
    "required": ["email", "source"],
    "properties": {
    "email": {"bsonType": "string"},
    "source": {"enum": ["web", "store"]}
    }
}})

db.newsletter_signups.insert_one({"email": "example@email.com", "source": "web"})
# The examples below will fail the validation and will not be inserted
#db.newsletter_signups.insert_one({"email": "hello", "source": "telephone"})
#db.newsletter_signups.insert_one({"email": "example@email.com"})
#db.newsletter_signups.insert_one({"source": "web"})
#db.newsletter_signups.insert_one({"email": "", "source": ""})

# Exercise 4
result = db.customers.aggregate([
    {"$group": {"_id": "$city",
                "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
])

for row in result:
    print(row)

# Exercise 5
result = db.products.aggregate([
    {"$group": {"_id": "$category",
                "min": {"$min": "$price"},
                "max": {"$max": "$price"}}}
])

for row in result:
    print(row)

# Exercise 6
result = db.orders.aggregate([
    {"$group": {"_id": "$customer_id",
                "count": {"$sum": 1}}},
    {"$match": {"count": {"$gte": 2}}}
])

for row in result:
    print(row)

# Exercise 7
result = db.orders.aggregate([
    {"$project": {"_id": True,
                "items": {"$size": "$items"}}}
])

for row in result:
    print(row)

# Exercise 8
result = db.orders.aggregate([
    {"$match": {
        "status": {"$ne": "cancelled"}
        }
    },
    {"$project": {
        "items.product_id": True,
        "items.quantity": True
        }
    },
    {"$unwind": "$items"},
    {"$lookup": {
        "from": "products",
        "localField": "items.product_id",
        "foreignField": "_id",
        "as": "product_data",
        }  
    },
    {"$project": {
        "items.product_id": True,
        "items.quantity": True,
        "product_data.category": True
        }
    },
    {"$group": {
        "_id": "$product_data.category", 
        "count": {"$sum": 1}
        }
    }
])

for row in result:
    print(row)

# Exercise 9
result = db.orders.aggregate([
    {"$project": {
        "status": True,
        "items.product_id": True,
        "items.quantity": True,
        "items.unit_price": True
        }
    },
    {"$unwind": "$items"},
    {"$lookup": {
        "from": "products",
        "localField": "items.product_id",
        "foreignField": "_id",
        "as": "product_data",
        }  
    },
    {"$project": {
        "status": True,
        "items.product_id": True,
        "items.quantity": True,
        "items.unit_price": True,
        "product_data.category": True
        }
    },
    {"$group": {
        "_id": "$status", 
        "count": {"$sum": 1},
        "revenue": {"$sum": {"$multiply": ["$items.quantity", "$items.unit_price"]}}
        }
    }
])

for row in result:
    print(row)

# Exercise 10
result = db.products.aggregate([
    {"$project": {
        "tags": True,
    }},
    {"$unwind": "$tags"},
    {"$group": {
        "_id": "$tags", 
        "count": {"$sum": 1}
    }},
    {"$sort": {
        "count": -1
        }
    }
])

for row in result:
    print(row)