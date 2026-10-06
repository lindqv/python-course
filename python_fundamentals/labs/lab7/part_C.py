class Product:
    tax_rate = 0.2

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + self.tax_rate * self.price

products = [
    Product("Chocolate cupcake", 30),
    Product("Carrot cake", 25),
    Product("Custom decorated cake", 200)
]

for product in products:
    print(product.price_with_tax())

products[-1].tax_rate = 0.3
print("Modified product tax rate", products[-1].tax_rate)
print("Standard product tax rate", products[0].tax_rate)
print("Product class tax rate", Product.tax_rate)