from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Movie(BaseModel):
    title: str
    director: str
    year: int

movies = [
    {"id": 1, "title": "Metropolis", "director": "Fritz Lang", "year": 1927},
    {"id": 2, "title": "Dead Poets Society", "director": "Peter Weir", "year": 1989},
    {"id": 3, "title": "Orlando", "director": "Sally Potter", "year": 1992},
    {"id": 4, "title": "Bright Star", "director": "Jane Campion", "year": 2009},
]

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    if director and year:
        return [movie for movie in movies 
                if director.lower() in movie["director"].lower() and year == movie["year"]]
    elif director:
        return [movie for movie in movies if director.lower() in movie["director"].lower()]
    elif year:
        return [movie for movie in movies if year == movie["year"]]
    else:
        return movies

@app.get("/movies/{id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    new_id = max((movie["id"] for movie in movies), default=0) + 1
    new_movie = {'id': new_id, 'title': movie.title, 'director': movie.director, 'year': movie.year}
    movies.append(new_movie)
    return new_movie