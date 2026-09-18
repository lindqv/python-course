def merge_settings(defaults, **overrides):
    pass

def call_summary(function_name: str, *args, **kwargs) -> str:
    return f"{function_name}({', '.join(args)}, {kwargs})"

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


print(call_summary("test", "arg1", "arg2", "arg3", extra=True))
print(statistics(1,2,3))
print(statistics(-100, 100))
print(statistics(77, 60, 90, 87))


