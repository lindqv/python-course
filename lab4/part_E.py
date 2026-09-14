def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature in degrees Celsius to degrees Fahrenheit.
    """
    return celsius * 9 / 5 + 32

def temperature_classification(temperature_celsius: float) -> str:
    if temperature_celsius < 10:
        return "Cold"
    elif temperature_celsius < 20:
        return "Warm"
    else:
        return "Hot"

def format_temperature(temperature, celsius=False, fahrenheit=False) -> str:
    if celsius:
        return f"{temperature} degrees C"
    elif fahrenheit:
        return f"{temperature} degrees F"
    else:
        return f"{temperature} degrees"

def temperature_report(temperature_celsius: float):
    print("Today's weather report")
    print(format_temperature(temperature_celsius, celsius=True))
    print(format_temperature(celsius_to_fahrenheit(temperature_celsius), fahrenheit=True))
    print(temperature_classification(temperature_celsius))

def subtotal(items: list[float]) -> float:
    return sum(items)

def calculate_discount(price: float, discount: float = 0) -> float:
    return price - price * (discount / 100)

def final_total(items: list[float], discount: float = 0) -> float:
    return calculate_discount(subtotal(items), discount)

if __name__ == "__main__":
    temperature_report(15.5)
    temperature_report(-5)
    temperature_report(30)
    print(final_total([100, 200]))
    print(final_total([100, 200], 20))
    print(final_total([100, 200, 300], 10))