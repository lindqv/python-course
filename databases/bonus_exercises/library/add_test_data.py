from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]

db.create_collection("books", validator={
    '$jsonSchema': {
        'bsonType': "object",
        'title': "Book Object Validation",
        'required': [ "title", "author", "copies" ],
        'properties': {
            'title': {
               'bsonType': "string",
               'description': "'title' must be a string and is required"
            },
            'author': {
                'bsonType': "string",
                'description': "'author' must be a string and is required"
            },
            'copies': {
               'bsonType': "int",
               'minimum': 0,
               'description': "'copies' must be an integer greater than or equal to 0, and is required"
            },
        }
    }
})

db.books.create_index( { "title": 1 } )


db.create_collection("members", validator={
    '$jsonSchema': {
        'bsonType': "object",
        'title': "Member Object Validation",
        'required': [ "name", "email" ],
        'properties': {
            'name': {
               'bsonType': "string",
               'description': "'name' must be a string and is required"
            },
            'email': {
                'bsonType': "string",
                'uniqueItems': True,
                'pattern': "^[a-zA-Z0-9._%+\\-]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,}$",
                'description': "'email' must be a valid email address and is required"
            },
        }
    }
})

db.create_collection("loans", validator={
    '$jsonSchema': {
        'bsonType': "object",
        'title': "Loan Object Validation",
        'required': [ "member_id", "book_id", "loaned_until", "returned" ],
        'properties': {
            'member_id': {
               'bsonType': "objectId",
               'description': "'member_id' must be an object id, and is required"
            },
            'book_id': {
                'bsonType': "objectId",
                'description': "'book_id' must be an object id, and is required"
            },
            'loaned_until': {
                'bsonType': "date",
                'description': "'loaned_until' must be an date, and is required"
            },
            'returned': {
                'bsonType': "bool",
                'description': "'returned' must be a boolean and is required"
            },
        }
    }
})

book_ids = [ObjectId() for _ in range(9)]
books = [
    {"_id": book_ids[0], "title": "Orlando", "author": "Virginia Woolf", "genre": "Fiction", "copies": 1},
    {"_id": book_ids[1], "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "genre": "Fiction", "copies": 4},
    {"_id": book_ids[2], "title": "Hamlet", "author": "William Shakespeare", "genre": "Plays", "copies": 0,},
    {"_id": book_ids[3], "title": "Frankenstein", "author": "Mary Shelley", "genre": "Fiction", "copies": 2},
    {"_id": book_ids[4], "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Fiction", "copies": 1},
    {"_id": book_ids[5], "title": "A Study in Scarlet", "author": "Arthur Conan Doyle", "genre": "Fiction", "copies": 0},
    {"_id": book_ids[6], "title": "Childe Harold's Pilgrimage", "author": "Lord Byron", "genre": "Poetry", "copies": 1,},
    {"_id": book_ids[7], "title": "Endymion", "author": "John Keats", "genre": "Poetry", "copies": 1},
]

member_ids = [ObjectId() for _ in range(2)]
members = [
    {"_id": member_ids[0], "name": "Anna", "email": "anna@example.com"},
    {"_id": member_ids[1], "name": "Anthony", "email": "anthony@example.com"},
]

loans = [
    {"member_id": member_ids[0], "book_id": book_ids[3], "loaned_until": datetime(2026, 10, 31), "returned": False},
]

db.books.insert_many(books)
db.members.insert_many(members)
db.loans.insert_many(loans)

print("Library is ready:",
      db.books.count_documents({}), "books,",
      db.members.count_documents({}), "members,",
      db.loans.count_documents({}), "loans")