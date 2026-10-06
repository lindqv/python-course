def calculate_total_minutes(sessions):
    total = 0
    for session in sessions:
        total += session["minutes"]

    return total

def minutes_per_subject(sessions):
    dictionary = {}

    for session in sessions:
        subject = session["subject"]
        minutes = session["minutes"]

        if subject in dictionary:
            dictionary[subject] = dictionary[subject] + minutes
        else:
            dictionary[subject] = minutes

    return dictionary

def longest_session(sessions):
    largest = None
    for session in sessions:
        if largest is None or session["minutes"] > largest:
            largest = session["minutes"]
    
    return largest

def print_sessions_longer_than(threshold, sessions):
    for session in sessions:
        if session["minutes"] > threshold:
            print(session)

def print_all_sessions(sessions):
    for session in sessions:
        print(session)

def print_filtered_sessions(sessions):
    target = input("Enter your subject to filter by: ").strip().lower()
    for session in sessions:
        if session["subject"].lower() == target:
            print(session)

def menu(sessions):
    user_input = ""

    while user_input != "quit":
        print("1. View all sessions")
        print("2. View total time")
        print("3. Filter by subject")
        print("Or type 'quit' to exit.")
        user_input = input("Enter your choice by typing an integer: ").strip().lower()

        if user_input == "1":
            print_all_sessions(sessions)
        elif user_input == "2":
            print(calculate_total_minutes(sessions))
        elif user_input == "3":
            print_filtered_sessions(sessions)

if __name__ == "__main__":
    study_sessions = [
        {
            "subject" : "Painting",
            "minutes" : 30
        },
        {
            "subject" : "Painting",
            "minutes" : 90
        },
        {
            "subject" : "Cooking",
            "minutes" : 45
        },
        {
            "subject" : "Poetry",
            "minutes" : 20
        },
        {
            "subject" : "Painting",
            "minutes" : 75
        },
        {
            "subject" : "Poetry",
            "minutes" : 100
        },
        {
            "subject" : "Painting",
            "minutes" : 30
        },
        {
            "subject" : "Cooking",
            "minutes" : 45
        },
        {
            "subject" : "Cooking",
            "minutes" : 20
        },
        {
            "subject" : "Poetry",
            "minutes" : 23
        },
    ]

    print(calculate_total_minutes(study_sessions))
    print(minutes_per_subject(study_sessions))
    print(longest_session(study_sessions))
    print_sessions_longer_than(45, study_sessions)
    menu(study_sessions)
    