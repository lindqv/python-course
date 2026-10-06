def is_even(number):
    return number % 2 == 0

def get_larger(a, b):
    if a > b:
        return a
    else:
        return b

def classify_score(score, threshold = 70):
    if score > threshold:
        return "PASS"
    else:
        return "FAIL"

def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def print_full_name(first_name, last_name):
    print(f"{first_name} {last_name}")

def calculate_discount(price, percent):
    return price - price * (percent / 100)

print(is_even(28))
print(is_even(7))
print(get_larger(5,7))
print(get_larger(4,2))
classify_score(88)
classify_score(50)
print(full_name("Ada", "Lovelace"))
name = print_full_name("Ada", "Lovelace") 
print(name) # This prints None, since the print_full_name does not return a value.
print(calculate_discount(300, 15))