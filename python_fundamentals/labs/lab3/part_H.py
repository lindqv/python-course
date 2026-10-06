from collections import Counter

def fizz_buzz(start: int, end: int):
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", i)
        elif i % 3 == 0:
            print("Fizz", i)
        elif i % 5 == 0:
            print("Buzz", i)

def count_vowels(sentence: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0

    for character in sentence:
        if character.lower() in vowels:
            vowel_count += 1
    return vowel_count

def duplicates(list: list) -> list:
    duplicates = []
    seen = []

    for item in list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.append(item)

    return duplicates

def duplicates_with_collections(list: list) -> list:
    list_counter = Counter(list)
    duplicates = []
    
    for item, count in list_counter.items():
        if count > 1:
            duplicates.append(item)

    return duplicates


def print_histogram(list: list[int]):
    for i in list:
        print('*' * i)


fizz_buzz(1, 100)
sentence = "Is this a good example? Here is also the letter U"
print(count_vowels(sentence))

list = [1, 3, 4, 3, 1, 1]
print(duplicates(list))
print(duplicates_with_collections(list))

print_histogram([3, 5, 2])