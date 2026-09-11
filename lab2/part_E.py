# 1. 
library = [
    {
        "title" : "Orlando",
        "author" : "Virginia Woolf",
        "pages" : 350,
        "available" : True,
    },
    {
        "title" : "The Picture of Dorian Gray",
        "author" : "Oscar Wilde",
        "pages" : 300,
        "available" : True,
    },
    {
        "title" : "Hamlet",
        "author" : "William Shakespeare",
        "pages" : 200,
        "available" : False,
    },
    {
        "title" : "Frankenstein",
        "author" : "Mary Shelley",
        "pages" : 250,
        "available" : True,
    },
    {
        "title" : "Pride and Prejudice",
        "author" : "Jane Austen",
        "pages" : 300,
        "available" : True,
    }
]

# 2.
print("Third book title", library[2]["title"])
print("Last book availability", library[-1]["available"])

# 3.
library[3]["available"] = False
library[1]["favourite"] = True

print(library)


# 4.
company = {
    "Finance" : ["Alice", "Bob", "Charlie"],
    "IT" : ["Daniel", "Eliza", "Fritz"]
}

# 5.
courses = [
    {
        "name" : "Cooking 101",
        "teacher" : "Daniel",
        "topics": ["ingredients", "frying pans", "seasoning", "nutrition", "recipe design"],
    },
    {
        "name" : "Painting",
        "teacher" : "Eliza",
        "topics": ["colour theory", "sketching", "art history", "mixing paint colours", "composition"],
    },
    {
        "name" : "Language learning",
        "teacher" : "Fritz",
        "topics": ["reading", "listening", "speaking", "translation", "grammar"],
    }
]