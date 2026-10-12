# Exercise 1-3

import sqlite3

connection = sqlite3.connect("webshop.db")
cursor = connection.cursor()

cursor.execute("SELECT first_name, last_name, city FROM customers")
for first_name, last_name, city in cursor.fetchall():
    print(f"{first_name} {last_name} ({city})")

max_price = input("Enter a max price: ")
cursor.execute("SELECT name, price FROM products WHERE price < ?", (max_price,))
for name, price in cursor.fetchall():
    print(f"{name} {price} kr")

category = input("Enter a category: ")
cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (category,))
print(cursor.fetchone()[0])

connection.close()

# Exercise 4
# Building SQL queries with an f-string allows for security vulnerabilities with SQL injections. 
# Using the ? placeholder prevents it,  so the database will interpret 
# the value supplied as just a value rather than code. 