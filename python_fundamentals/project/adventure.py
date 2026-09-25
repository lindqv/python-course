import random

class Ability:
    def __init__(self, ability_name: str, minimum_damage: int, maximum_damage: int, heal: int = 0):
        self.ability_name = ability_name
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage
        self.heal = heal

class Character:
    def __init__(self, name: str, health_points: int, level: int, armour_class: int, abilities: list[Ability]):
        self.name = name
        self.health_points = health_points
        self.max_health_points = health_points
        self.level = level
        self.armour_class = armour_class
        self.abilities = abilities

    def attack(self, target: 'Character', ability: Ability):
        if dice.roll(20) > target.armour_class:
            attack_damage = dice.roll(ability.maximum_damage, ability.minimum_damage)
            target.health_points -= attack_damage
            print(f"{self.name} attacked {target.name} with {ability.ability_name} for {attack_damage} damage")
        else:
            print(f"{self.name} attacked {target.name} with {ability.ability_name}, but missed")


class Dice:
    def __init__(self):
        random.seed()

    def roll(self, max: int, min: int=1) -> int:
        return random.randrange(min, max + 1)

    def choose_index(self, max: int) -> int:
        return random.randrange(max)


player_abilities = [Ability("Advanced attack", 4, 6), Ability("Basic attack", 2, 3)]
player = Character("Player", 10, 1, 15, player_abilities)

rat_abilities = [Ability("Bite", 2, 3), Ability("Screech", 1, 2)]
rat1 = Character("Rat 1", 5, 1, 10, rat_abilities)
rat2 = Character("Rat 2", 5, 1, 10, rat_abilities)
enemies = [rat1, rat2]

dice = Dice()

while player.health_points > 0 and enemies:
    print("New turn. Health status:")
    for participant in [player] + enemies:
        print(f"{participant.name}: {participant.health_points}/{participant.max_health_points} health points")
    
    enemy_to_attack = enemies[0]
    ability_to_use = player.abilities[dice.choose_index(len(player_abilities))]
    player.attack(enemy_to_attack, ability_to_use)
    
    if enemy_to_attack.health_points <= 0:
        enemies.remove(enemy_to_attack)
        print(enemy_to_attack.name, "was defeated!")
    
    for enemy in enemies:
        ability_to_use = enemy.abilities[dice.choose_index(len(enemy.abilities))]
        enemy.attack(player, ability_to_use)
    print("\n")

    if not enemies:
        print("Enemies defeated!")
    elif player.health_points <= 0:
        print("Player was defeated. Game over!")