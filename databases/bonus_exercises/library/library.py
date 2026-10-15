from pymongo import MongoClient
from pymongo.cursor import Cursor
client = MongoClient("mongodb://localhost:27017/")
db = client["library"]

def main():
    print("Welcome to the library!")
    while True:
        print("What would you like to do?")
        print("1. Search for books")
        print("2. Quit")
        choice = int(input("Choose by typing an integer: "))

        if choice == 1:
            query = input("Enter a search query: ")
            result = search_for_books(query)
            print_book_search_result(result)
        elif choice == 2:
            break

def search_for_books(query: str):
    result = db.books.find({"$text": {"$search": query}})
    return result

def print_book_search_result(result: Cursor):
    for entry in result:
        print(f"{entry.get('title', 'Untitled')} by {entry.get('author', 'Unknown author')}")
        print(f"{entry.get('genre', 'Unknown genre')}")
        print(f"{entry.get('copies', 0)} copies available")

main()