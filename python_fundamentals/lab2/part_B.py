# 1.
rgb = (255, 200, 85)
red, green, blue = rgb
print("red, green, blue", red, green, blue)

# 2.
person = ("Ada Lovelace", 33, "London")
name, age, city = person
print(f"{name} is {age} years old and lives in {city}")

# 3.
#person[2] = "Cambridge"
# The above line gives a type error, since tuples are immutable and do not support item assignment.
# Tuples are useful when values should not be changed, and will cause type errors if changes are attempted.

# 4.
coordinates = [(10, 20), (0,0), (34, 44), (-3, -7)]
for pair in coordinates:
    print(f"The position is now ({pair[0]}, {pair[1]})")