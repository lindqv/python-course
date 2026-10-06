# 1.
course_name = "Python"
def print_course_name():
    course_name = "Python and AI"
    print(course_name)

print("Global variable:", course_name) # Prints Python
# The below prints Python and AI, since we are inside the function and the scope of the local variable in it.
print("Local variable in the function:", print_course_name()) 

# 2.
def count():
    counter = 1
    print("Counting", counter)

# print(counter) # The counter variable is not defined outside of the function, so it cannot be used.

# 3.
number = 3
def increment(integer):
    # number = 4 # This creates a new local variable, does not affect the variables outside
    return integer + 1

number = increment(number)
print("Number is now", number)
# The above solution modifies the global variable by returning and reassigning.

# 4.
def outer():
    count = 7
    print("Outer count is", 7)
    def inner():
        print("Inner count is", count)

    inner()

outer()

# 5.
# A function that avoids shadowing the built-ins list and str
def print_strings(strings: list[str]):
    for string in strings:
        print(string)

# A function that avoids shadowing the built-ins list, sum
def calculate_total(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

# A function that avoids shadowing the built-ins list and max
def find_greatest_number(numbers: list[int]) -> int:
    greatest = None
    for number in numbers:
        if greatest is None or number > greatest:
            greatest = number
    return greatest