def loop_until_divisible(number_A, number_B, max, start = 1):
    for i in range(start, max + 1):
        print(i)
        if i % number_A == 0 and i % number_B == 0:
            break

def skip_empty_strings(strings):
    for string in strings:
        if string == "":
            continue

        print(string)

def search(target, list):
    found = False

    for item in list:
        if item == target:
            found = True
            print("Found!")
            break

    if not found:
        print("Not found, whole list searched through ")

def skip_negative_values(list):
    for number in list:
        if number == 999:
            print("Processing stopped")
            break
        elif number < 0:
            continue
        else:
            print("Processed", number)

if __name__ == "__main__":
    loop_until_divisible(7, 9, 100)
    skip_empty_strings(["", "hello", "hi", "good morning", "", "good evening", ""])
    search("blueberry", ["banana", "grapefruit", "strawberry", "blueberry", "pomegranate"])
    search("blueberry", [])
    search("apple", ["banana", "grapefruit", "strawberry", "blueberry", "pomegranate"])
    skip_negative_values([0, 1, -1, -4, 7, 5, -444, 999, 11])