from datetime import time

flights = [
    {
        "flight_number": "SK142",
        "destination": "London",
        "departure_time": time(14,30),
        "gate": "B4",
        "passengers": 132,
        "maximum_capacity": 180,
        "delay_in_minutes": 25,
        "cancelled": False,
    },
    {
        "flight_number": "SA798",
        "destination": "Stockholm",
        "departure_time": time(21,30),
        "gate": "D9",
        "passengers": 90,
        "maximum_capacity": 130,
        "delay_in_minutes": 0,
        "cancelled": True,
    },
    {
        "flight_number": "LH231",
        "destination": "Berlin",
        "departure_time": time(15,00),
        "gate": "A4",
        "passengers": 150,
        "maximum_capacity": 165,
        "delay_in_minutes": 0,
        "cancelled": False,
    },
    {
        "flight_number": "BA442",
        "destination": "Manchester",
        "departure_time": time(15,20),
        "gate": "C1",
        "passengers": 100,
        "maximum_capacity": 120,
        "delay_in_minutes": 93,
        "cancelled": False,
    },
]

def print_departure_board(flights):
    for flight in flights:
        print(f"{flight['flight_number']} - {flight['destination']} - {flight['departure_time']} - Gate {flight['gate']} - {get_status(flight)}")

def get_status(flight):
    if flight["cancelled"]:
        return "CANCELLED"
    elif flight["delay_in_minutes"] >= 60:
        return "SEVERELY DELAYED"
    elif flight["delay_in_minutes"] >= 20:
        return "DELAYED"
    elif flight["delay_in_minutes"] >= 1:
        return "SLIGHT DELAY"
    else:
        return "ON TIME"

def print_flight_data(flights):
    cancelled_flights = 0
    delayed_flights = 0
    flights_on_time = 0

    total_passengers = 0
    max_passengers = 0
    flight_with_most_passengers = ""

    percentage = 0.8
    flights_with_percentage_capacity_filled = 0

    for flight in flights:
        if flight["cancelled"]:
            cancelled_flights += 1
        if flight["delay_in_minutes"] > 0:
            delayed_flights += 1
        if flight["delay_in_minutes"] == 0:
            flights_on_time += 1

        total_passengers += flight["passengers"]

        if flight["passengers"] > max_passengers:
            max_passengers = flight["passengers"]
            flight_with_most_passengers = flight["flight_number"] 

        if flight["passengers"] / flight["maximum_capacity"] > percentage:
            flights_with_percentage_capacity_filled += 1

    print("Total number of scheduled flights:", len(flights))
    print("Candelled flights:", cancelled_flights)
    print("Delayed flights:", delayed_flights)
    print("Flights on time:", flights_on_time)
    print("Total number of passengers:", total_passengers)
    print("Average number of passengers per flight:", total_passengers / len(flights))
    print("Flight with the largest number of passengers", flight_with_most_passengers)
    print("Flights with more than 80 of their capacity filled", flights_with_percentage_capacity_filled)
    
if __name__ == "__main__":
    print_departure_board(flights)
    print_flight_data(flights)
