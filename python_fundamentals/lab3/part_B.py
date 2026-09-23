def truthy_falsy(value):
    if value:
        print(value, "is truthy")
    else:
        print(value, "is falsy")

def language_supported():
    supported_languages = ["python", "c", "rust"]
    language = input("Enter a language: ").strip().lower()

    if language in supported_languages:
        print("Your language is supported.")
    else:
        print("Your language is not supported.")

def username_allowed(username):
    blocked_usernames = ["a", "b", "c"]
    return username not in blocked_usernames

"""
Two readable conditions using not:

    username not in blocked_usernames   # as on line 18 
    number not in first_ten_prime_numbers
"""

if __name__ == "__main__":
    truthy_falsy("")
    truthy_falsy("hi")
    truthy_falsy(0)
    truthy_falsy(2)
    truthy_falsy([])
    truthy_falsy([4,7])

    print(username_allowed("test"))
    print(username_allowed("c"))

    language_supported()


