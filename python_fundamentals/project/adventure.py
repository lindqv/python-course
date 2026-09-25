class Ability:
    def __init__(self, ability_name: str, damage: int, heal: int = 0):
        self.ability_name = ability_name
        self.damage = damage
        self.heal = heal

class Character:
    def __init__(self, name: str, health_points: int, level: int, abilities: list[Ability]):
        self.name = name
        self.health_points = health_points
        self.level = level
        self.abilities = abilities

    def attack(self, target, ability: Ability): #todo: use character type
        target.health_points -= ability.damage
        print(f"{self.name} attacked {target.name} for {ability.damage} damage")

player_abilities = [Ability("Basic attack", 3)]
player = Character("Player", 10, 1, player_abilities)

rat_abilities = [Ability("Bite", 1)]
rat1 = Character("Rat", 5, 1, rat_abilities)
rat2 = Character("Rat", 5, 1, rat_abilities)
enemies = [rat1, rat2]

while player.health_points > 0:
    while enemies:
        print("New turn")
        enemy_to_attack = enemies[0]
        ability_to_use = player.abilities[0]
        player.attack(enemy_to_attack, ability_to_use)
        if enemy_to_attack.health_points <= 0:
            enemies.remove(enemy_to_attack)
        
        for enemy in enemies:
            enemy.attack(player, enemy.abilities[0])

    print("Enemies defeated")
    break