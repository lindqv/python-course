# 1.
laptop = {
    "brand" : "Framework",
    "model" : "13 Pro",
    "RAM" : 32,
    "price" : 15000,
}

# for value in laptop.values():
#    print(value)


# 2.
laptop["price"] = 10000
laptop["operating_system"] = "Linux"
laptop.pop("RAM")

# for value in laptop.values():
#    print(value)


# 3.
model = laptop.get("model")
colour = laptop.get("colour") # Using get for a key that does not exist does not cause an error
print(model, colour)

laptop["model"] # This line works fine since the key exists
# laptop["colour"] # This line causes a key error since the key does not exist


# 4.
print("Keys")
for key in laptop.keys():
   print(key)

print("Values")
for value in laptop.values():
   print(value)

print("Items")
for item in laptop.items():
   print(item)


# 5.
study_log = {
   "Mathematics" : 30,
   "Computer Science" : 40,
   "Geoology" : 10,
   "Philosophy" : 7,
   "Biology" : 8,
}

print("Total hours", sum(study_log.values()))