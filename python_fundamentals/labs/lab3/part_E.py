def countdown(counter = 10, lower_limit = 0):
    while counter >= lower_limit:
        print(counter)
        counter -= 1

def password():
    password = "loop"
    user_input = ""

    while user_input != password:
        user_input = input("Please enter the password: ")

def menu():
    user_input = ""
    options = ["Ice cream", "Chocolate", "Cinnamon roll"]

    while user_input != "quit":
            print("Menu options: ")
            for index, option in enumerate(options):
                print(f"{index + 1}. {option}")
                 
            user_input = input("Please enter a number, or type quit to exit. ").lower()

            if user_input.isdigit():
                 print(f"You chose option {user_input}. {options[int(user_input) - 1]}")

def sum_user_input():
    sum = 0
    user_input = None

    while user_input != "0": 
        user_input = input("Enter an integer: ")

        if user_input.isdigit():
            sum += int(user_input)

    print("The sum of the entered integers is", sum)

def guess_secret_number(secret_number):
    user_input = None

    while user_input != secret_number:
        user_input = int(input("Guess the secret number! "))

        if user_input > secret_number:
            print("Your guess is too high.")
        elif user_input < secret_number:
            print("Your guess is too low.")
        else:
            print("You found the secret number!")


if __name__ == "__main__":
    guess_secret_number(7)