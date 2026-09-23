names = ["Gregory", "Sam", "Penelope"]
scores = [7, 5, 10]
pairs = zip(names, scores)
for pair in pairs:
    print(pair)

dictionary = dict(zip(names, scores))
print(dictionary)

product_names = ["milk", "eggs", "bread"]
prices = [15, 40, 30]
in_stock = [False, True, True]
products = zip(product_names, prices, in_stock)
for product in products:
    print(product)

product_names = ["milk", "eggs", "bread", "chocolate", "apples"]
products = zip(product_names, prices, in_stock)
for product in products: # Still prints 3 items, zip ends after the shortest iterable ends
    print(product)

zipped = zip([1,2,3], [4,5,6])
for a, b in zipped:
    print("Unpacked tuple", a, b)

a = 10
b = 5
print("Before, a =", a, "b =", b)
b, a = a, b
print("After, a =", a, "b =", b)
