class Printer:
    def __init__(self, status: str):
        self.status = status

    def display_status(self):
        return "Printer status " + self.status

class Screen:
    def __init__(self, status: str):
        self.status = status

    def display_status(self):
        return "Screen status " + self.status

objects = [Printer("working"), Screen("in repair")]

for object in objects:
    print(object.display_status())

# This works because each object in the list has the display_status() method.
# With duck typing the presence of a method (or attribute) is the important part, 
# rather than which type the objects have.
# The duck test: "If it walks like a duck and quacks like a duck, then it must be a duck."