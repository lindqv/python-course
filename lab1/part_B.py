def calculate_age():
    name = input("Please input your name: ") 
    birth_year = int(input("What is your year of birth? "))
    current_year = 2026
    print("The approximate age of", name ,"is", current_year - birth_year)

def calculate_price():
    price = float(input("Enter the price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = price * (100 - discount_percentage) / 100
    print(f"The final price is {final_price:.2f}")

def celsius_to_fahrenheit():
    celsius = float(input("Please enter a temperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print("The temperature in Fahrenheit is", fahrenheit)

def calculate_area_perimeter():
    length = float(input("Please input the length: "))
    width = float(input("Please input the width: "))
    area = length * width
    perimeter = 2 * length + 2 * width
    print(f"The area is {area:.2f} and the perimeter is {perimeter:.2f}")

if __name__ == "__main__":
    calculate_area_perimeter()
    
# 5. 
# If the user inputs invalid input where a numeric input is expected, a value error will occur.
# For example: the function calculate_area_perimeter():
# If the user inputs "hello", the float conversion will fail with a value error:
# ValueError: could not convert string to float: 'hello'