numbers = list(range(1,21))
squares = []
for number in numbers:
    squares.append(number * number)
print("Squares with loop", squares)
print("Squares with list comprehension", [number * number for number in numbers])

evens = [number for number in range(1,101) if number % 2 == 0]
print("Even numbers", evens)

names = ["ada", "   grace ", "alan "]
processed_names = [name.strip().title() for name in names]
print("Processed names", processed_names)

scores = [99, 97, 73, 56, 69, 44]
passing_scores = [score for score in scores if score >= 70]
print("Passing scores", passing_scores)

score_labels = ["PASS" if score >= 70 else "FAIL" for score in scores]
print("Score labels", score_labels)

# Rewriting three earlier loop-based transformations as list comprehensions:
# 1. skip_empty_strings
strings = ["", "aaa", "bbb", "", "ccc", "", ""]
non_empty_strings = [string for string in strings if string != ""]
print(non_empty_strings)

# 2. skip_negative_values
values = [0, 1, -1, -4, 7, 5, -444, 999, 11]
non_negative_values = [value for value in values if value >= 0]
print(non_negative_values)

# 3. get_long_words
limit = 7
words = ["exquisite", "dragon", "beautiful", "gem"]
long_words = [word for word in words if len(word) >= limit]
print(long_words)
