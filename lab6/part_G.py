list_of_lists = [["hello", "hi"], ["greetings", "good day"], ["bye"]]
flattened_list = [item for sublist in list_of_lists for item in sublist]

# Flattening the list with a for loop, for comparison:
flattened_list_loop = []
for sublist in list_of_lists:
    for item in sublist:
        flattened_list_loop.append(item)

limit = 10
multiplication_table = [[x * y for x in range(1, limit + 1)] for y in range(1, limit + 1)]

# I think this multiplication table code is readable enough. 
# If the readability question refers to the printing output of the multiplicaion table,
# it could be made more readable by making sure the numbers in the columns are aligned.


names = ["Anna", "Bianca", "Christopher"]
scores = [67, 90, 87]
passing_students = [{"name": name, "score": score} 
                    for name, score in zip(names, scores) 
                    if score > 70]

scores = [55, -5, -22, -7, 0, -44, -11, 88, 7]

has_non_zero_value_loop = False
all_zero_or_empty_loop = True
for score in scores:
    if score != 0:
        has_non_zero_value_loop = True
        all_zero_or_empty_loop = False

has_non_zero_value = any(scores)
all_zero_or_empty = all(scores)


print("Flattened list", flattened_list)
print("Flattened list loop", flattened_list_loop)
for row in multiplication_table:
    print(row)

print("Passing students", passing_students)

print("Scores", scores)
print("Has non-zero value, with loop:", has_non_zero_value_loop)
print("Has non-zero value, with any():", has_non_zero_value)
print("All zero, or empty, with loop:", all_zero_or_empty_loop)
print("All zero, or empty, with all():", all_zero_or_empty)



