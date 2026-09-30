from characters import Enemy
from items import Item

class Room:
    def __init__(self, enemies: list[Enemy], items: list[Item] = None):
        self.enemies = enemies
        if items is None:
            self.items = []
        else:
            self.items = items

    def remove_enemy(self, enemy: Enemy):
        self.enemies.remove(enemy)

    def has_enemies(self) -> bool:
        return len(self.enemies) > 0

class Dungeon:
    def __init__(self, rooms: list[Room]):
        self.rooms = rooms