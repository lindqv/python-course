# 1.
languages = ["Python", "Java", "C", "C++", "C#", "Rust", "Go", "R"]
print("First element", languages[0])
print("Third element", languages[2])
print("Second-to-last element", languages[-2])

# 2.
print(languages[2:5])
print(languages[-3:])
print(languages[:3])

# 3.
languages.append("JavaScript")
print(languages)
languages.remove("C#")
print(languages)
languages.pop()
print(languages)

# 4. 
numbers = [1, 1, 2, 3, 5, 8, 13, 21]
print("Length", len(numbers))
print("Minimum", min(numbers))
print("Maximum", max(numbers))
print("Sum", sum(numbers))

# 5.
sort_me = [-3, -77, 4, 7, 2, 0, 65, 234]
sort_me_too = [54, 4859, -3, 1, 12, -7, -99]
sort_me.sort()
sort_me_too.sort(reverse=True)

print("Ascending sort", sort_me)
print("Descending sort", sort_me_too)

# .sort() sorts the list in place, modifying the list. 
# .sorted() does not modify the original list, but returns a new sorted list.

example = [5, 2, 8]
sorted_example = sorted(example)
print("Unsorted example", example)
print("Sorted example", sorted_example)


# 6. 
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_b = list_a.copy()
list_a.pop()

print("List A", list_a) 
print("List B", list_b)

# Having line 48 without copy() results in both lists being [1, 2] even though only list A was modified.
# Using copy fixes this so list B is unchanged when list A is changed. 