# Part A
# 1.
print("Name: Sanne Lindqvist")
print("Course name: Python and AI")
print("Today's study goal: Review Python basics")

# 2.
name = "Ada Lovelace"
age = 32
height = 1.65
currently_student = False

for variable in [name, age, height, currently_student]:
    print(f"The variable has value {variable} and is of type {type(variable)}")

# 3. 
my_variable = "hello"
print("The type of my variable before is ", type(my_variable))
my_variable = 57
print("The type of my variable after is, ", type(my_variable))
# This demonstrates that Python is dynamically typed, 
# therefore allowing a variable to be reassigned with 
# a type that is different to the one it had previously.

# 4. 
a = 10
b = 3

print("Addition", a + b)
print("Subtraction", a - b)
print("Multiplication", a * b)
print("Division", a / b)
print("Floor division", a // b)
print("Remainder", a % b)
print("Exponentation", a ** b)

# 5.
# string to int
user_input = "5052"
remainder = int(user_input) % 2
print("The remainder is", remainder)

# int to float
price = 5 
print("The price is", float(price))

# number to string
number = 44
concatenation = "33" + str(number)
print("The concatenation is", concatenation)