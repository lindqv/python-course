from quests import Quest, DefeatEnemiesObjective, RoomVisitObjective

default_quests = [
    Quest("Defeat 3 enemies", DefeatEnemiesObjective(3)),
    Quest("Defeat 5 enemies", DefeatEnemiesObjective(5)),
    Quest("Defeat 10 enemies", DefeatEnemiesObjective(10)),
    Quest("Visit 4 rooms", RoomVisitObjective(4)),
    Quest("Visit 7 rooms", RoomVisitObjective(7))
    ]
