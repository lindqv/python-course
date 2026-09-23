class Teacher:
    def __init__(self, name: str):
        self.name = name

class Student:
    def __init__(self, name: str):
        self.name = name

class Course:
    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        self.teacher = teacher
        self.students: list[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)


teacher = Teacher("Grace Hopper")
course = Course("Compilers", teacher)

print("Course name:", course.name)
print("Teacher name:", course.teacher.name)

student1 = Student("Scout")
student2 = Student("Arabella")
student3 = Student("Tamino")

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

for student in course.students:
    print(student.name)