class Teacher:
    def __init__(self, name: str):
        self.name = name

class Course:
    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student: dict):
        self.students.append(student)

teacher = Teacher("Grace Hopper")
course = Course("Compilers", teacher)

print("Course name:", course.name)
print("Teacher name:", course.teacher.name)

course.add_student({"name": "Scout"})
course.add_student({"name": "Arabella"})
course.add_student({"name": "Tamino"})

for student in course.students:
    print(student.get("name"))