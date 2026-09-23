class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return self.name

class Developer(Employee):
    def write_code(self):
        print(self.name, "is writing code")

class Archivist(Employee):
    def organize_archive(self):
        print(self.name, "is organizing the archive")

developer = Developer("Anna")
archivist = Archivist("Anthony")
employee = Employee("Alina")

# The subclasses can use inherited behaviour from Employee:
print(developer.get_information())
print(archivist.get_information())

# But an employee cannot use subclass methods. These lines give an AttributeError.
# employee.write_code()
# employee.organize_archive()
