from fastapi import FastAPI, HTTPException

app = FastAPI()

movies = [
    {"id": 1, "title": "Metropolis", "director": "Fritz Lang", "year": 1927},
    {"id": 2, "title": "Dead Poets Society", "director": "Peter Weir", "year": 1989},
    {"id": 3, "title": "Orlando", "director": "Sally Potter", "year": 1992},
    {"id": 4, "title": "Bright Star", "director": "Jane Campion", "year": 2009},
]

@app.get("/movies")
def get_movies():
    return movies

@app.get("/movies/{id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")