# 1.
def sum_three(a: int, b: int, c: int) -> int:
    return a + b + c

numbers = [10, 20, 30]
print(sum_three(*numbers))

# 2.
first_name = "Ada"
last_name = "Lovelace"
city = "London"
tuple = (first_name, last_name, city)
def print_info(a, b, c):
    print(a)
    print(b)
    print(c)

print_info(*tuple)

# 3.
first, *middle, last = [1, 2, 3]
print("First", first, "Middle", middle, "Last", last)
first, *middle, last = [1, 2, 3, 4, 5, 6, 7, 575838]
print("First", first, "Middle", middle, "Last", last)
# first, *middle, last = [] # Having fewer values in the list than variables gives a value error.

# 4.
# * in a function definition indicates that the function accepts a variable number of arguments.
#   It combines multiple values into a single tuple.
# * in a function call unpacks the values of an iterable before passing them to the function.
#   This allows the function to recieve each value separately, rather than as a single list, tuple, or similar.