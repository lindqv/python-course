class DefeatEnemiesObjective:
    def __init__(self, goal_count: int):
        self.goal_count = goal_count

    def is_complete(self, current_count: int):
        return current_count >= self.goal_count

class RoomVisitObjective:
    def __init__(self, goal_count: int):
        self.goal_count = goal_count

    def is_complete(self, current_count: int):
        return current_count >= self.goal_count

class Quest:
    def __init__(self, description: str, objective: DefeatEnemiesObjective | RoomVisitObjective, is_complete: bool = False):
        self.description = description
        self.objective = objective
        self.is_complete = is_complete

    def __str__(self):
        return f"{self.description} - {'Complete' if self.is_complete else 'Not complete'}"
    
    def complete(self):
        self.is_complete = True

class QuestLog:
    def __init__(self, quests: list[Quest]):
        self.quests = quests

    def show_status(self):
        print("\n")
        print("Quest log:")
        if len(self.quests) == 0:
            print("There are no quests.")

        for quest in self.quests:
            print(quest)

    def update_quests(self, defeated_enemies: int, visited_rooms: int):
        for quest in self.quests:
            if quest.is_complete:
                continue

            elif isinstance(quest.objective, DefeatEnemiesObjective):
                if quest.objective.is_complete(defeated_enemies):
                    quest.complete()

            elif isinstance(quest.objective, RoomVisitObjective):
                if quest.objective.is_complete(visited_rooms):
                    quest.complete()
