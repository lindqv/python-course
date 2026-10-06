def seconds_converter():
    total_seconds = int(input("Please enter your time in seconds: "))

    hours = total_seconds // (60 * 60)
    hours_in_seconds = hours * 60 * 60
    minutes = (total_seconds - hours_in_seconds) // 60
    seconds = total_seconds % 60 

    print(f"{hours} h, {minutes} m, {seconds} s")


def print_digits():
    four_digit_integer = int(input("Please enter a four-digit integer: "))
    first_digit = four_digit_integer // 1000
    second_digit = four_digit_integer // 100 - first_digit * 10
    third_digit = four_digit_integer // 10 - first_digit * 100 - second_digit * 10
    final_digit = four_digit_integer % 10

    print("First digit", first_digit)
    print("Second digit", second_digit)
    print("Third digit", third_digit)
    print("Final digit", final_digit)

def text_masking(display_before = 2, display_after = 2):
    text = input("Please enter a word to mask: ")

    if len(text) <= display_before + display_after:
        print(text)
    else:
        prefix = text[:display_before]
        stars = "*" * (len(text) - (display_before + display_after))
        suffix = text[-display_after:]
        print(f"{prefix}{stars}{suffix}")


# 4. Predict before running exercises
"""
    print(type(str(42))) # <class 'str'>
    print("baguette"[:3]) # bag
    print("croissant"[-3:]) # ant
    print("croissant"[4:6]) # ss
    print("croissant"[:-3] + "baguette"[-4:]) # croissette
"""

if __name__ == "__main__":
    text_masking()
