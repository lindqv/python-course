class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, price: {self.price}"


cakes = [Product("Chocolate cake", 30), Product("Strawberry cake", 35), Product("Blueberry cake", 35)]

for cake in cakes:
    print(cake)

readable_cake = str(cakes[0])
print(type(readable_cake))