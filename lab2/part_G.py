# 1.
usernames_A = ["test", "alice", "bob", "charlie"]
usernames_B = ["test", "charlie", "delia"]
all_usernames = usernames_A + usernames_B
unique_usernames = set(all_usernames)
duplicate_usernames = set([name for name in all_usernames if name in usernames_A and name in usernames_B])

print("Unique usernames:", unique_usernames)
print("Duplicate usernames:", duplicate_usernames)

# 2.
course_platform = [
    {
        "name" : "Cooking 101",
        "teacher" : "Daniel",
        "topics": ["ingredients", "frying pans", "seasoning", "nutrition", "recipe design"],
        "students": ["Gabriel, Harriet"],
    },
    {
        "name" : "Painting",
        "teacher" : "Eliza",
        "topics": ["colour theory", "sketching", "art history", "mixing paint colours", "composition"],
        "students": ["Gabriel, Isa, Jacob"],
    },
    {
        "name" : "Language learning",
        "teacher" : "Fritz",
        "topics": ["reading", "listening", "speaking", "translation", "grammar"],
        "students": ["Jacob, Harriet", "Isa"],
    }
]

# 3.
inventory = [
    {
        "name": "Baguette",
        "count": 5,
    },
    {
        "name": "Croissant",
        "count": 7,
    },
    {
        "name": "Soufflé",
        "count": 3
    },
    {
        "name": "Éclair",
        "count": 5
    },
    {
        "name": "Pain au chocolat",
        "count": 4
    },
]

inventory[0]["count"] = 7
inventory[-1]["count"] = 3

total = 0
for item in inventory:
    total += item["count"]

print("Total in inventory:", total)

# 4.
"""
List: for ordered items where accessing by index is useful.
Example: For storing a sequence of integers, and sorting it.

Tuple: for organising data in an immutable, ordered format.
Example: For storing coordinates.

Set: for collections of unordered items where uniqueness is important.
Example: For keeping track of unique usernames.

Dictionary: For key-value pairs, where you can access a value by providing a key.
Example: For storing the model and specs of a computer.
"""