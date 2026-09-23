tracks = ["Track A", "Track B", "Track C"]
for index, track in enumerate(tracks, start=1):
    print(f"{index}. {track}")

tasks = ["Start the dishwasher", "Have a snack", "Rest"]
for index, task in enumerate(tasks, start=1):
    print(f"Task {index}: {task}")

threshold = 10
values = [3, 4, 34, 22, 7, 11, 10, 9, 777]
for index, value in enumerate(values):
    if value > threshold:
        print(index)

for index in range(len(values)):
    print(index, values[index])

for index, value in enumerate(values):
    print(index, value)

# The version of the for loop on line 18 is clearer than the one on line 15,
# since it does not need nesting of range and len, or square brackets to access a value.