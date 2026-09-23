def greet(greeting = "Hello"):
    print(greeting)

def print_separator(separator = "-", separator_length = 10):
    print(separator * separator_length)

def show_course_name(course):
    print(course["name"])

def greet_person(name, greeting = "Hello"):
    print(greeting, name)

def introduce(name, city):
    print("This is", name, "from", city)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): # Parameters: here a and b are the parameters of this function.
    return a / b

def calculate_area(width, height):
    return width * height

greet()
greet("Good morning")
print_separator()
show_course_name({"name": "Python", "hours": 20})
show_course_name({"name": "Rust", "hours": 10})
print_separator()
print(divide(5, 2)) # Arguments: here 5 and 2 are the arguments given to this function.
area_a = calculate_area(5, 5)
area_b = calculate_area(10, 2)
print("The total area is", area_a + area_b)