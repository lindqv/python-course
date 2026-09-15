def log_event(event_type, *messages, **metadata):
    event = {"event_type": event_type}
    event["messages"] = messages
    event["metadata"] = metadata
    return event

def calculate_order(customer, *prices, **options):
    total = sum(prices)
    shipping_fee = options.get("shipping_fee", 0)
    discount = options.get("discount", 0)
    return total - total * discount/100 + shipping_fee


# Comparing the readability of kwargs vs. named arguments
# I think it is kwargs is useful when there is a variable number of arguments, and it is important that each of them has a keyword.
# I'd argue that named arguments is more readable, clearer in terms of what (and how many arguments) to expect, and clearer to give type hints to.
# Both are useful, but during different circumstances.

def total_value_kwargs(**kwargs):
    total = 0
    for value in kwargs.values():
        total += value
    return total

def total_value(values):
    total = 0
    for value in values:
        total += value
    return total


print(log_event("login", "hello", "test message", "logging", timestamp="16:29", day="today"))

print(total_value_kwargs(a=1, b=2))
print(total_value([1,2]))

# Three calls with different numbers of arguments
print(calculate_order("Ada", 100, 300, 999, shipping_fee=50, discount=20))
print(calculate_order("Grace", 1000, shipping_fee=100, discount=0))
print(calculate_order("Alan", 100, 300, 100, 200))