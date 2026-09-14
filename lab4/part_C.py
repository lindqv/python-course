def greet(name, greeting = "Hello"):
    print(greeting, name)

def calculate_price(price, quantity=1, discount=0):
    return (price - price * (discount / 100)) * quantity

def create_profile(name, city="Unknown", active=True):
    return { "name": name, "city": city, "active": active}

# Invalid default parameter order example, non-default parameter follows default parameter
# def create_profile(city="Unknown", name, active=True):
#    return { "name": name, "city": city, "active": active}

greet("Ada")
greet("Ada", greeting="Good afternoon")
greet("Ada", "Good evening")
print(calculate_price(300, 2, 15))
print(create_profile("Ada", "London"))
print(create_profile(active=False, name="Ada"))