def classify_number(number):
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Number is zero")

def classify_age(age):
    if age < 10:
        print("Age is less than 10")
    elif age < 20:
        print("Age is between 10 and 20")
    elif age < 30:
        print("Age is between 20 and 30")
    elif age < 40:
        print("Age is between 30 and 40")
    else:
        print("Age is greater than 40")

def login():
    username = "guido"
    password = "python"
    username_input = input("Username: ")
    password_input = input("Password: ")

    if username_input == username and password_input == password:
        print("You are logged in.")
    else:
        print("Username, password or both were incorrect.")

def grade(score):
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    elif score >= 70:
        print("Grade C")
    elif score >= 60:
        print("Grade D")
    elif score >= 50:
        print("Grade E")
    else:
        print("Grade F")

def calculate_shipping(order_total, is_member):
    if order_total >= 300 or (order_total >= 200 and is_member):
        return 0
    else:
        return 39

"""
Boolean examples to predict before running:
"hello" == "HELLO"  # False
3 != 3.0            # False
7 > 4               # True
7 < 4               # False
11 <= 11            # True
11 >= 7             # True
"""

if __name__ == "__main__":
    classify_number(0)
    classify_number(4)
    classify_number(-99)

    classify_age(8)
    classify_age(28)
    classify_age(35)
    classify_age(43)
    classify_age(55)

    grade(99)
    grade(87)
    grade(73)
    grade(66)
    grade(52)
    grade(42)

    print(calculate_shipping(99, True))
    print(calculate_shipping(304, False))
    print(calculate_shipping(200, True))

    login()
