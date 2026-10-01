class Quest:
    def __init__(self, goal: str, is_complete: bool = False):
        self.goal = goal
        self.is_complete = is_complete

    def __str__(self):
        return f"{self.goal} - {'Complete' if self.is_complete else 'In progress'}"
    
    def complete(self):
        self.is_complete = True

class QuestLog:
    def __init__(self, quests: list[Quest]):
        self.quests = quests

    def show_status(self):
        for quest in self.quests:
            print(quest)




    