import sys, json, os, time
sys.path.append("..")
from part1.api_client import get_json

def find_city(city_name: str):
    return get_json("https://geocoding-api.open-meteo.com/v1/search", params={"name": city_name, "count": 1})

def get_weather(latitude: float, longitude: float):
    return get_json("https://api.open-meteo.com/v1/forecast", params={
        "latitude": latitude, 
        "longitude": longitude, 
        "current": ["temperature_2m", "wind_speed_10m"]
        }
    )

def get_cache_data(cache_path: str, cache_age_minutes_limit: int = 10):
    if os.path.exists(cache_path):
        time_last_modified_seconds = os.path.getmtime(cache_path)
        time_now_seconds = time.time()
        cache_age_minutes = (time_now_seconds - time_last_modified_seconds) / 60
        print("cache age minutes", cache_age_minutes)

        if cache_age_minutes < cache_age_minutes_limit:
            with open(cache_path, mode="r", encoding="utf-8") as cache:
                cache_data =  json.load(cache)
                print("got data from the cache")
                return cache_data
    print("no cache")

def write_to_cache(cache_path: str, json_data):
    with open(cache_path, mode="w", encoding="utf-8") as cache:
        json.dump(json_data, cache)

def valid_cache_coordinate_response(coordinate_response, city_name: str):
    if coordinate_response is None:
        return False
    else:
        return coordinate_response["results"][0]["name"] == city_name

def valid_weather_response(weather_response, city_name: str):
    if weather_response is None:
        return False
    return weather_response.get("city") == city_name

def main():
    print("Current weather service")
    city = input("Enter a city to show the weather for: ").strip().title()

    coordinate_cache_path = "cache_coordinates.json"
    coordinate_response = get_cache_data(coordinate_cache_path)
    if not valid_cache_coordinate_response(coordinate_response, city):
        coordinate_response = {}
    
    if not coordinate_response:
        print("calling the coordinate api for", city)
        coordinate_response = find_city(city)
        write_to_cache(coordinate_cache_path, coordinate_response)

    if coordinate_response.get("results"):
        latitude = coordinate_response["results"][0]["latitude"]
        longitude = coordinate_response["results"][0]["longitude"]
        country = coordinate_response["results"][0]["country"]

        weather_cache_path = "cache_weather.json"
        weather_response = get_cache_data(weather_cache_path)
        if not valid_weather_response(weather_response, city):
            print("cache data was not valid for", city, weather_response)
            weather_response = {}

        if not weather_response:
            print("calling the weather api")
            weather_response = get_weather(latitude, longitude)
            weather_response_with_city_name = {**weather_response, "city": city}
            print("weather data with city name", weather_response_with_city_name)
            write_to_cache(weather_cache_path, weather_response_with_city_name)

        if weather_response:
            temperature = weather_response["current"]["temperature_2m"]
            temperature_unit = weather_response["current_units"]["temperature_2m"]
            wind_speed = weather_response["current"]["wind_speed_10m"]
            wind_speed_unit = weather_response["current_units"]["wind_speed_10m"]

        print(f"{city}, {country}: {temperature} {temperature_unit}, wind {wind_speed} {wind_speed_unit}")
    
    else:
        print("Could not find the city.")

main()

# Task 3
# Adding a cache to avoid calling an API too often is useful because: 
# * It decreases the number of API calls (hopefully avoiding rate limits)
# * It is faster to fetch data from a file than to make an API call