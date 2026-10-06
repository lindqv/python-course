class Book:
    def __init__(self, title: str, author: str, pages: int = 0):
        self.title = title
        self.author = author
        self.pages = pages

books = [
    Book("Orlando", "Virginia Woolf", 350),
    Book("The Picture of Dorian Gray", "Oscar Wilde", 300),
    Book("Hamlet", "William Shakespeare", 200),
    Book("Frankenstein", "Mary Shelley", 250),
    ]

for book in books:
    print(book.title, book.author, book.pages)


class Laptop:
    def __init__(self, brand: str, model: str, ram_gb: int, price: float):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Framework", "13 Pro", 32, 15000)
laptop2 = Laptop("HP", "Envy", 16, 10000)
laptop3 = Laptop("Framework", "13 Pro", 32, 15000)
laptop2.price = 8000

print(laptop1.price, laptop2.price, laptop3.price)

print("Are two objects with the same attribute values the same object?", laptop1 is laptop3)
print("Are two objects with the same attribute values equal?", laptop1 == laptop3)

laptop4 = Laptop(brand="HP", model="A new one", ram_gb=32, price=12000)