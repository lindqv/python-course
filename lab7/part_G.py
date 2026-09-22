class Teacher:
    def __init__(self, name: str):
        self.name = name

class Student:
    def __init__(self, name: str, score: int):
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.name = name
        self.score = score

    def grade(self) -> str:
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"

    def update_score(self, new_score: int):
        if new_score < 0:
            raise ValueError("Score cannot be negative")
        self.score = new_score

class Course:
    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        self.teacher = teacher
        self.students: list[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def student_count(self) -> int:
        return len(self.students)

    def passed_students(self) -> list[Student]:
        return [student for student in self.students if student.grade() == "PASS"]

    def students_above_score_threshold(self, threshold: int) -> list[Student]:
            return [student for student in self.students if student.score >= threshold]

teacher = Teacher("Grace Hopper")
course = Course("Compilers", teacher)

student1 = Student("Scout", 88)
student2 = Student("Arabella", 90)
student3 = Student("Tamino", 68)
student4 = Student("Percy", 73)
student5 = Student("Sophie", 70)

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
course.add_student(student4)
course.add_student(student5)

student3.update_score(74)
print("Score is now", student3.score)

print("Students with scores above 80")
for student in course.students_above_score_threshold(80):
    print(student.name)
