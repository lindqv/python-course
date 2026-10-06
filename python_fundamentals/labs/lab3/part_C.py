def numbered_greeting(names):
    for number, name in enumerate(names, start = 1):
        print(f"{number}. Hello {name}!")

def print_evens(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

def sum(list):
    sum = 0
    for value in list:
        sum += value

    return sum

def max(list):
    largest = None
    for element in list:
        if largest is None or element > largest:
            largest = element

    return largest

def count_words_longer_than(words, limit):
    count = 0
    for word in words:
        if len(word) > limit:
            count += 1
    return count

def count_grades(scores, threshold):
    passes = 0
    fails = 0

    for score in scores:
        if score >= threshold:
            passes += 1
        else:
            fails += 1

    print("Passes", passes)
    print("Fails", fails)

def print_dictionary(dict):
    for key in dict.keys():
        print(key)

    for value in dict.values():
        print(value)

    for item in dict.items():
        print(item)


if __name__ == "__main__":
    numbered_greeting(["Alice", "Bob", "Charlie"])
    print_evens(1, 50)
    print(sum([1,2,3]))
    print(max([1,3,2]))
    print(max([]))
    print(count_words_longer_than(["hello", "this", "is", "an", "example"], 5))
    count_grades([70, 50, 90, 0], 70)

    print_dictionary(
        {
            "bread" : 10,
            "cake" : 7,
         }
    )

    print_dictionary(
        {
            "up" : 1,
            "down" : -1,
            "left" : 2,
            "right" : -2
        }
    )

    print_dictionary(
        {
            "tomatoes" : 3,
            "carrots" : 5,
            "apples": 7,
        }
    )