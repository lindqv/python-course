# Exercises 5-8

import sqlite3
 
 
def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
 
 
def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")
 
 
def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)
 
 
def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")

def change_stock(conn):
    product_id = int(input("Product id: "))
    new_stock = int(input("New stock amount: "))
    conn.execute("UPDATE products SET stock = ? WHERE product_id = ?", (new_stock, product_id))
    conn.commit()
    print("Saved!")


def show_order_reciept(conn):
    order_id = int(input("Order id: "))
    cursor = conn.execute("SELECT p.name, oi.quantity, p.price, oi.quantity * p.price " \
                            "FROM orders o " \
                            "JOIN order_items oi ON oi.order_id = o.order_id " \
                            "JOIN products p ON p.product_id = oi.product_id " \
                            "WHERE o.order_id = ?",
                            (order_id,))
    rows = cursor.fetchall()
    
    if rows:
        print("Reciept for order", order_id)
        print(f"{'Name':<20} {'Quantity':<10} {'Unit price':<10} {'Line total':<10}")
    for (product_name, quantity, unit_price, line_total) in rows:
        print(f"{product_name:<20} {quantity:<10} {unit_price:<10} {line_total:<10}")

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product  " \
        "4) Change stock of product  5) Show order reciept  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_order_reciept(conn)
        elif choice == "0":
            break
    conn.close()
 
 
main()