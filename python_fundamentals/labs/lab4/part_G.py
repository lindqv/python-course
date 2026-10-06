def min_max(list: list[int]) -> tuple[int, int]:
    """
    Returns the minimum and maximum values of a list of integers.
    """

    min = None
    max = None

    for item in list:
        if min is None or item < min:
            min = item
        if max is None or item > max:
            max = item

    return (min, max)

def palindrome(word: str) -> bool:
    """
    Checks if a word is a palindrome.
    """
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return palindrome(word[1:-1])

def character_frequencies(string: str) -> dict[str, int]:
    """
    Counts how many times each character occurs in a string.
    """
    frequencies = dict()
    for character in string:
        if character in frequencies.keys():
            frequencies[character] += 1
        else:
            frequencies[character] = 1

    return frequencies

def count_sign(list: list[int]) -> dict[str, int]:
    """
    Counts how many positive integers, negative integers, and zeroes there are in a list.
    """
    counts = {
        "positive": 0,
        "negative": 0,
        "zero": 0,
    }

    for number in list:
        if number > 0:
            counts["positive"] += 1
        elif number < 0:
            counts["negative"] += 1
        else:
            counts["zero"] += 1

    return counts


print(min_max([3,2,1,0,10,-3]))
print(min_max([]))
print(min_max.__doc__)
print(palindrome("banana"))
print(palindrome("annana"))
print(palindrome("anna"))
print(palindrome("racecar"))
print(palindrome("kayak"))
print(palindrome("tacocat"))
print(character_frequencies("Exquisite dragon, beautiful gem"))
print(character_frequencies(""))
print(count_sign([3, -4, 0, -2, -11, 44]))