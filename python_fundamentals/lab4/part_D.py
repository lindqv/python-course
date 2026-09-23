def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def count_even(numbers):
    evens = 0
    for number in numbers:
        if number % 2 == 0:
            evens += 1
    return evens

def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)
    return long_words

def find_student(students, name):
    for student in students:
        if name in student.values():
            return student
    return None

def average_score(students):
    total = 0
    for student in students:
        total += student.get("score")
    return total / len(students)

def get_active_users(users):
    return filter(lambda user : user.get("active"), users)

print(calculate_total([1,2,3]))
print(count_even([1,2,3,4,5,6]))
print(get_long_words(["exquisite", "dragon", "beautiful", "gem"], 7))

students = [
    {
        "name": "Ada",
        "score": 99,
        "active": True,
    },
    {
        "name": "Grace",
        "score": 98,
        "active": False,
    },
    {
        "name": "Alan",
        "score": 97,
        "active": True,
    },
]
print(find_student(students, "Grace"))
print(average_score(students))
print(students[0].get("age"))
for user in get_active_users(students):
    print(user.get("name"), "is active")
