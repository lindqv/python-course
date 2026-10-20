import sys
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
def main():
    print("Current weather service")
    city = input("Enter a city to show the weather for: ")
    coordinate_response = find_city(city)

    if coordinate_response.get("results"):
        latitude = coordinate_response["results"][0]["latitude"]
        longitude = coordinate_response["results"][0]["longitude"]
        country = coordinate_response["results"][0]["country"]

        weather_response = get_weather(latitude, longitude)
        print(weather_response)
        if weather_response:
            temperature = weather_response["current"]["temperature_2m"]
            temperature_unit = weather_response["current_units"]["temperature_2m"]
            wind_speed = weather_response["current"]["wind_speed_10m"]
            wind_speed_unit = weather_response["current_units"]["wind_speed_10m"]

        print(f"{city}, {country}: {temperature} {temperature_unit}, wind {wind_speed} {wind_speed_unit}")
    
    else:
        print("Could not find the city.")

main()
