squares = {number : number * number for number in range(1,11)}
print(squares)

words = ["hello", "good afternoon", "hi"]
word_lengths = {word : len(word) for word in words}
print(word_lengths)

duplicates = ["hello", "hello", "HI", "good afternoon", " hi ", "hi", "   HI "]
uniques = {word.strip().lower() for word in duplicates}
print(uniques)

products = ["milk", "bread", "eggs"]
prices = [15, 30, 40]
threshold = 35
products_below_threshold = {product : price for product, price in zip(products, prices) if price < threshold}
print(products_below_threshold)

students = [
    {
        "name": "Alice",
        "score": 99,
    },
    {
        "name": "Bob",
        "score": 87,
    },
    {
        "name": "Charlie",
        "score": 67,
    },
]

threshold = 70
student_results = {
    student.get("name"): 
    ("PASS" if student.get("score") >= threshold else "FAIL")
    for student in students
}
print(student_results)