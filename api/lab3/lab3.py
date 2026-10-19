from dotenv import load_dotenv
import os
import sys
sys.path.append("..")
from lab1.api_client import get_json
import requests

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

username = input("Enter a GitHub username: ")
response = get_json(f"https://api.github.com/users/{username}/repos", 
         params={"sort": "pushed", "per_page": 5},
         headers={"Authorization": f"Bearer {token}"})

for repo in response:
    print(repo.get("name"))

response = requests.get(f"https://api.github.com/users/{username}/repos", 
                        params={"sort": "pushed", "per_page": 5}, 
                        headers={"Authorization": f"Bearer {token}"}, 
                        timeout=5)

print("Rate limit with token", response.headers.get("X-RateLimit-Limit"))

response = requests.get(f"https://api.github.com/users/{username}/repos", 
                        params={"sort": "pushed", "per_page": 5}, 
                        timeout=5)

print("Rate limit without token", response.headers.get("X-RateLimit-Limit"))