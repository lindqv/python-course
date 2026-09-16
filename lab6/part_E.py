words = ["dragon", "gem", "adventure", "sword"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)

students = [
    {"name": "Ada", "score": 98},
    {"name": "Grace", "score": 97},
    {"name": "Alan", "score": 99},
]

sorted_by_score_ascending = sorted(students, key=lambda student: student.get("score"))
sorted_by_score_descending = sorted(students, key=lambda student: student.get("score"), reverse=True)
print(sorted_by_score_ascending)
print(sorted_by_score_descending)

products = [
    {"name": "eggs", "price": 40},
    {"name": "bread", "price": 35},
    {"name": "milk", "price": 15},
]

products_by_price = sorted(products, key=lambda product: product.get("price"))
print(products_by_price)

def sort_product(product: dict) -> int | None:
    return product.get("price")

products_by_price_named_function = sorted(products, key=sort_product)
print(products_by_price_named_function)

# Comparing the readability of soring with a lambda function or a named function,
# on lines 22 and 25-28:
# I think the named function is clearer, and more readable.
# The lambda function however is shorter since it does not need a separate function defintion.
# If the sorting is only used in a single place in the code or if I prefer a compact solution, 
# then I would use the lambda function.
# If I am reusing the sorting function in many places, I would usually prefer a named function.
