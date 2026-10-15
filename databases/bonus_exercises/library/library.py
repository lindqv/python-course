from pymongo import MongoClient
from pymongo.cursor import Cursor
from bson.objectid import ObjectId
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]

def main():
    print("Welcome to the library!")
    while True:
        print("What would you like to do?")
        print("1. Search for books")
        print("2. View all loans")
        print("3. View overdue loans")
        print("4. Quit")
        choice = int(input("Choose by typing an integer: "))

        if choice == 1:
            query = input("Enter a search query: ")
            result = search_for_books(query)
            print_book_search_result(result)
        if choice == 2:
            result = get_all_loans()
            print_loans(result)
        if choice == 3:
            result = get_overdue_loans()
            print_loans(result)
        elif choice == 4:
            break

def search_for_books(query: str):
    return db.books.find({"$text": {"$search": query}})

def print_book_search_result(result: Cursor):
    for entry in result:
        print(f"{entry.get('title', 'Untitled')} by {entry.get('author', 'Unknown author')}")
        print(f"{entry.get('genre', 'Unknown genre')}")
        print(f"{entry.get('copies', 0)} copies available")

def get_all_loans():
    return db.loans.find()

def get_overdue_loans():
    current_date = datetime.now()
    return db.loans.find({"loaned_until" : {"$lt": current_date}})

def get_loan_by_id(member_id: ObjectId):
    return db.loans.find({"member_id": member_id})

def print_loans(result: Cursor):
    for item in result:
        print("Book id", item.get("book_id"))
        print(f"Loaned until {item.get('loaned_until').date()}")
        print(f"{'Returned' if item.get('returned') else 'Not returned'}")

main()