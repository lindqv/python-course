def show_profile(**info):
    for data in info.items():
        print(data)

dictionary = {"a": 1, "b": 2, "c": 3}
show_profile(**dictionary)
show_profile(a=1, b=2, c=3)

def create_user(username, **details):
    user = {"username": username}
    for key, value in details.items():
        user[key] = value
    return user

print(create_user("grace", active=False))
details = {"active": True, "email": "ada@example.com"}
print(create_user("ada33", **details))

def build_product(name, price, **metadata):
    product = {"name": name, "price": price}
    for key, value in metadata.items():
        product[key] = value
    return product

metadata = {"shelf": "A33", "colour": "red"}
print(build_product("T-shirt", "199", **metadata))

def active_settings(**settings):
    active_settings = dict()
    for key, value in settings.items():
        if value is not None:
            active_settings[key] = value
    return active_settings

settings = {"sound": True, "wifi": None, "charging": False}
print(active_settings(**settings))

def add(a, b, c):
    return a + b + c

dictionary = {"a": 4, "b": 5, "c": 6}
print(add(**dictionary))