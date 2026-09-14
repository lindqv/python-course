def create_participant(name: str, age: int, student: bool) -> dict:
    return {
        "name": normalize_participant_name(name),
        "age": age,
        "student": student,
    }

def normalize_participant_name(name: str) -> str:
    return name.strip()

def validate_age_range(age: int, range_start: int, range_end: int) -> bool:
    return age >= range_start and age <= range_end

def calculate_registration_fee(participant: dict) -> int:
    if participant.get("student"):
        return 0
    elif validate_age_range(participant.get("age"), 65, 130):
        return 50
    else:
        return 100

def calculate_total_registration_revenue(participants: list[dict]) -> int:
    revenue = 0
    for participant in participants:
        revenue += calculate_registration_fee(participant)
    
    return revenue

def get_student_participants(participants: list[dict]) -> list[dict]:
    students = []
    for participant in participants:
        if participant.get("student"):
            students.append(participant)

    return students

def get_oldest_participant(participants: list[dict]) -> dict:
    oldest_participant = None
    for participant in participants:
        if oldest_participant is None or participant.get("age") > oldest_participant.get("age"):
            oldest_participant = participant
    
    return oldest_participant
        
def print_participant(participant: dict):
    print("Name: ", participant.get("name"))
    print("Age: ", participant.get("age"))
    if participant.get("student"):
        print("Student")


participants = []
participants.append(create_participant("Ada", 33, False))
participants.append(create_participant("Grace", 88, False))
participants.append(create_participant("Alan", 40, False))
participants.append(create_participant("Patricia", 24, True))
participants.append(create_participant("Sebastian", 27, True))
participants.append(create_participant("Felix", 33, True))
participants.append(create_participant("Edgar", 39, False))
participants.append(create_participant("Moira", 43, False))

print(calculate_total_registration_revenue(participants))
for student in get_student_participants(participants):
    print(student.get("name"), "is a student")

print_participant(get_oldest_participant(participants))
