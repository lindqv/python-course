movie_dictionary = {
    "title": "Metropolis",
    "director": "Fritz Lang",
    "rating": 8.2,
}

class Movie:
    def __init__(self, title: str, director: str, rating: float):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        return self.rating >= 8.0

movie_class = Movie("Metropolis", "Fritz Lang", 8.2)
print(movie_class.is_highly_rated())

# Dictionary vs. class
# If I wanted to simply store key-value pairs, I would use a dictionary.
# If I wanted to store data about a movie (in any format) and have methods associated with it,
# I would choose a class. 