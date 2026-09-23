def merge_settings(defaults: dict, **overrides) -> dict:
    merged = dict()
    for key, value in defaults.items():
        override_value = overrides.get(key)
        if override_value:
            merged[key] = override_value
        else:
            merged[key] = value

    return merged

def call_summary(function_name: str, *args, **kwargs) -> str:
    kwargs_formatted = [f"{item[0]} = {item[1]}" for item in kwargs.items()]
    return f"{function_name}({', '.join(args)}, {', '.join(kwargs_formatted)})"

def statistics(*numbers):
    count = len(numbers)
    total = 0
    min = None
    max = None

    for number in numbers:
        total += number
        if min is None or number < min:
            min = number
        if max is None or number > max:
            max = number

    average = total / count
    return count, total, average, min, max


default_settings = {
    "theme": "light",
    "language": "English",
    "month": "September"
}

new_settings = merge_settings(default_settings, theme="dark", language="Swedish")
print(new_settings)

print(call_summary("test", "arg1", "arg2", "arg3", extra=True, data=[1,2,3]))

print(statistics(1,2,3))
print(statistics(-100, 100))
print(statistics(77, 60, 90, 87))

# Five scope questions and their output:

# 1. Output is "hi"
greeting = "hello"
def greet():
    greeting = "hi"
    print(greeting)

greet()

# 2. Output is "hello"
greeting = "hello"
def greet():
    greeting = "hi"
    return greeting

greet()
print(greeting)

# 3. Output is "hi"
global new_greeting
new_greeting = "hello"
def greet():
    new_greeting = "hi"
    print(new_greeting)

greet()

# 4. Output is "hi"
greeting = "hello"
def greet():
    greeting = "hi"

    def inner_greet():
        print(greeting)

    inner_greet()

greet()

# 5. Output is "hello"
greeting = "hello"
def greet():
    greeting = "hi"

    def inner_greet():
        greeting = "hello again"

    inner_greet()

greet()
print(greeting)


