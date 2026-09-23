class Student:
    def __init__(self, name: str, score: int):
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.name = name
        self.score = score

    def get_status(self) -> str:
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"

    def update_score(self, new_score: int):
        if new_score < 0:
            raise ValueError("Score cannot be negative")
        self.score = new_score


student1 = Student("Scout", 88)
student2 = Student("Arabella", 90)
student3 = Student("Tamino", 68)
student4 = Student("Percy", 73)
student5 = Student("Sophie", 70)
student6 = Student("Rosalind", 80)

students = [student1, student2, student3, student4, student5, student6]

for student in students:
    print(student.name, student.score, student.get_status())

students_score_above_70 = [student for student in students if student.score >= 70]