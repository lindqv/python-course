# 1.
course_list = ["Mathematics", "Computer Science", "Philosophy", "Geology", "Biology", "Mathematics", "Computer Science", "Computer Science"]
course_set = set(course_list)
print("Length before and after", len(course_list), len(course_set))
print("Course set", course_set)


# 2.
developer_A = {"Python", "Java", "C", "Haskell"}
developer_B = {"Python", "R", "JavaScript", "Rust"}
print("Shared skills", developer_A & developer_B)
print("Skills only developer A has", developer_A - developer_B)
print("Skills only developer B has", developer_B - developer_A)
print("All skills", developer_A | developer_B)
print("Skills that only one developer has", developer_A ^ developer_B)


# 3.
fruits = set()
fruits.add("Banana")
fruits.add("Orange") 
fruits.add("Kiwi")
print("Fruit set after adding", fruits)

fruits.remove("Orange")
print("Fruit set after removing", fruits)

print("Is orange in the set?", "Orange" in fruits)
print("Is kiwi in the set?", "Kiwi" in fruits)

# 4.
"""
A set is a better choice than a list if we want to ensure unique values,
and if it not important for items to be ordered.

For instance, to keep track of unique usernames.
"""