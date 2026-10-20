from api_client import get_json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE = "http://127.0.0.1:8000"

all_movies = get_json(f"{BASE}/movies")
print(all_movies)

response = get_json(f"{BASE}/movies/77")

new_movie = {
    "title": "The Lord of the Rings: The Fellowship of the Ring",
    "director": "Peter Jackson",
    "year": 2001,
}
response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
print("Without key", response.status_code)

response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5, 
                         headers={"X-API-Key": API_KEY})
print("With key", response.status_code)