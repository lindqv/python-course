from datetime import datetime
from pymongo import MongoClient

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

books = [
    {"_id": 1, "title": "Orlando", "author": "Virginia Woolf", "genre": "Fiction", "copies": 1},
    {"_id": 2, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "genre": "Fiction", "copies": 4},
    {"_id": 3, "title": "Hamlet", "author": "William Shakespeare", "genre": "Plays", "copies": 0,},
    {"_id": 4, "title": "Frankenstein", "author": "Mary Shelley", "genre": "Fiction", "copies": 2},
    {"_id": 5, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Fiction", "copies": 1},
    {"_id": 6, "title": "A Study in Scarlet", "author": "Arthur Conan Doyle", "genre": "Fiction", "copies": 0},
    {"_id": 7, "title": "Childe Harold's Pilgrimage", "author": "Lord Byron", "genre": "Poetry", "copies": 1,},
    {"_id": 8, "title": "Endymion", "author": "John Keats", "genre": "Poetry", "copies": 1},
]

members = [
    {"_id": 1, "name": "Anna", "email": "anna@example.com"},
    {"_id": 2, "name": "Anthony", "email": "anthony@example.com"},
]

loans = [
    {"member_id": 1, "book_id": 4, "loaned_until": datetime(2026, 10, 31), "returned": False},
]

db.books.insert_many(books)
db.members.insert_many(members)
db.loans.insert_many(loans)

print("Library is ready:",
      db.books.count_documents({}), "books,",
      db.members.count_documents({}), "members,",
      db.loans.count_documents({}), "loans")
