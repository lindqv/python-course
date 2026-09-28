from characters import Character
from items import Item

class Room:
    def __init__(self, enemies: list[Character], items: list[Item] = None):
        self.enemies = enemies
        if items:
            self.items = items
        else:
            items = []

    def remove_enemy(self, enemy: Character):
        self.enemies.remove(enemy)

    def has_enemies(self) -> bool:
        return len(self.enemies) > 0

class Dungeon:
    def __init__(self, rooms: list[Room]):
        self.rooms = rooms