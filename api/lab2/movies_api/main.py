from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
import os, json

load_dotenv()
API_KEY = os.getenv("API_KEY")
MOVIES_PATH = "movies.json"

app = FastAPI()

class Movie(BaseModel):
    title: str
    director: str
    year: int

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

def check_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401)

def find_movie(movie_id: int):
    movies = load_movies(MOVIES_PATH)
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

def find_movie_index(movie_id: int):
    movies = load_movies(MOVIES_PATH)
    for index, movie in enumerate(movies):
        if movie['id'] == movie_id:
            return index

def load_movies(path: str):
    if os.path.exists(path):
        with open(path, mode="r", encoding="utf-8") as movies:
            return json.load(movies)
    else:
        return [
            {"id": 1, "title": "Metropolis", "director": "Fritz Lang", "year": 1927},
            {"id": 2, "title": "Dead Poets Society", "director": "Peter Weir", "year": 1989},
            {"id": 3, "title": "Orlando", "director": "Sally Potter", "year": 1992},
            {"id": 4, "title": "Bright Star", "director": "Jane Campion", "year": 2009},
        ]

def save_movies(path: str, json_data):
    with open(path, mode="w", encoding="utf-8") as movies:
        json.dump(json_data, movies, indent=2)

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    movies = load_movies(MOVIES_PATH)

    if director and year:
        return [movie for movie in movies 
                if director.lower() in movie["director"].lower() and year == movie["year"]]
    elif director:
        return [movie for movie in movies if director.lower() in movie["director"].lower()]
    elif year:
        return [movie for movie in movies if year == movie["year"]]
    else:
        return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)

@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def create_movie(movie: Movie):
    movies = load_movies(MOVIES_PATH)
    new_id = max((movie["id"] for movie in movies), default=0) + 1
    new_movie = {'id': new_id, 'title': movie.title, 'director': movie.director, 'year': movie.year}
    movies.append(new_movie)
    save_movies(MOVIES_PATH, movies)
    return new_movie

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing['title'] = movie.title
    existing['director'] = movie.director
    existing['year'] = movie.year
    return existing


@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)

@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id: int, movie_update: MovieUpdate):
    existing = find_movie(movie_id)
    fields_to_update = movie_update.model_dump(exclude_unset=True)
    for (key, new_value) in fields_to_update.items():
        existing[key] = new_value
    return existing

# Testing response codes
# Empty body {}: 200, no change
# Year written as text: 422
# Id that does not exist: 404

# PATCH vs PUT
# I would use PATCH if I wanted to update only some of the fields.
# I would use PUT if I wanted to complete replace all the values with new ones, 
# keeping none of the old values.