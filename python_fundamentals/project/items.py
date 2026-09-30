import random

class Dice:
    def __init__(self):
        random.seed()

    def roll(self, min: int=1, max: int=20) -> int:
        return random.randrange(min, max + 1)

    def choose_index(self, max: int) -> int:
        return random.randrange(max)

class Item:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Weapon(Item):
    def __init__(self, name: str, damage_bonus: int):
        super().__init__(name)
        self.damage_bonus = damage_bonus

class Armour(Item):
    def __init__(self, name: str, armour_class: int):
        super().__init__(name)
        self.armour_class = armour_class

class HealthPotion(Item):
    def __init__(self, name: str, healing: int):
        super().__init__(name)
        self.healing = healing

    def use(self, player):
        player.health_points = min(player.health_points + self.healing, player.max_health_points)
        player.inventory.remove(self)
        print("Player health points is now", player.health_points)