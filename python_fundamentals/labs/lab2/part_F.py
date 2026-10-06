library = [
    {
        "title" : "Orlando",
        "author" : "Virginia Woolf",
        "pages" : 350,
        "available" : True,
        "category" : "Fiction",
        "year": 1928,
        "id" : 1,
    },
    {
        "title" : "The Picture of Dorian Gray",
        "author" : "Oscar Wilde",
        "pages" : 300,
        "available" : True,
        "category" : "Fiction",
        "year": 1890,
        "id" : 2,
    },
    {
        "title" : "Hamlet",
        "author" : "William Shakespeare",
        "pages" : 200,
        "available" : False,
        "category" : "Plays",
        "year": 1601,
        "id" : 3,
    },
    {
        "title" : "Frankenstein",
        "author" : "Mary Shelley",
        "pages" : 250,
        "available" : True,
        "category" : "Fiction",
        "year": 1818,
        "id" : 4,
    },
    {
        "title" : "Pride and Prejudice",
        "author" : "Jane Austen",
        "pages" : 300,
        "available" : True,
        "category" : "Fiction",
        "year": 1813,
        "id" : 5,
    },
    {
        "title" : "A Study in Scarlet",
        "author" : "Arthur Conan Doyle",
        "pages" : 400,
        "available" : False,
        "category" : "Fiction",
        "year": 1887,
        "id" : 6,
    },
    {
        "title" : "Childe Harold's Pilgrimage",
        "author" : "Lord Byron",
        "pages" : 200,
        "available" : True,
        "category" : "Poetry",
        "year": 1818,
        "id" : 7,
    },
    {
        "title" : "Endymion",
        "author" : "John Keats",
        "pages" : 250,
        "available" : True,
        "category" : "Poetry",
        "year": 1818,
        "id" : 8,
    },
]

categories = set()
tuples = []
for book in library:
    categories.add(book["category"])
    tuples.append((book["id"], book["year"]))

print(categories)
print(tuples)

library[0]["available"] = False
print(library[3]["title"], library[3]["year"], library[3]["author"])
print(library[-1]["title"], library[-1]["year"], library[-1]["author"])
print("Poetry" in categories)
print("Non-fiction" in categories)
library.sort(key = lambda book : book['title'])


print("Catalogue summary:")
for book in library:
    print(f"{book['title']} by {book['author']}, {book['year']}")
    print(f"{book['category']} category, {book['pages']} pages")
    print(f"{'Available' if book['available'] else 'Not available'}", end='\n\n')