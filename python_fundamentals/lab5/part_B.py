def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def average(*numbers):
    if len(numbers) == 0:
        return 0

    return add_all(*numbers) / len(numbers)

def longest_word(*words):
    if len(words) == 0:
        return None

    longest_word = words[0]
    for word in words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def build_sentence(separator, *words):
    sentence = ""
    for index, word in enumerate(words):
        if index == len(words) - 1:
            sentence = sentence + word
        else:
            sentence = sentence + word + separator
    return sentence

def describe_scores(student_name, *scores):
    return student_name, len(scores), average(*scores)

print(add_all(1,2,3))
print(add_all(1,2,3,4,5,6,7,8,9))
print(average(1,2,3))
print(average())
print(longest_word("apple", "banana", "kiwi"))
print(longest_word("banana", "apple", "kiwi"))
print(longest_word("kiwi", "apple", "banana"))
print(longest_word())
print(build_sentence(",", "apple", "banana", "kiwi"))
print(describe_scores("Ada", 70, 80, 99))