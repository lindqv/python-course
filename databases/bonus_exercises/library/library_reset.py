from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]

for name in ["books", "members", "loans"]:
    db[name].drop()

print("Library is reset:",
      db.books.count_documents({}), "books,",
      db.members.count_documents({}), "members,",
      db.loans.count_documents({}), "loans")
