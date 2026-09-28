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