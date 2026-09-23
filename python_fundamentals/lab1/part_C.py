def sentence_transform():
    sentence = "    This is a VERY interesting sentence.  "
    print("The sentence has length", len(sentence))
    print("Uppercase:", sentence.upper())
    print("Lowercase:", sentence.lower())
    print("Without whitespace:", sentence.strip())

def print_full_name():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print(f"Your full name is {first_name.strip()} {last_name.strip()}")

def string_slicing():
    string = "python programming"
    print("First character:", string[0])
    print("Last character:", string[-1])
    print("Everything except the last character:", string[:-1])
    print("First six characters:", string[:6])
    print("Last eleven characters:", string[-11:])
    print("Reversed:", string[::-1])

def username_generator():
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    username = first_name[:3] + last_name[:5]
    print("Your username is", username)


def email_address_parts():
    email = "hello@gmail.com"
    before, after = email.split('@')
    print("Before:", before, "After:", after)

def replace_word():
    sentence = "I am learning Java today"
    target = "Java"
    replacement = "Python"
    replaced_sentence = sentence.replace(target, replacement)
    print("Original sentence:", sentence)
    print("Changed sentence:", replaced_sentence)


if __name__ == "__main__":
    replace_word()