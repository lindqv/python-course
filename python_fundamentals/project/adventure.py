import random

class Ability:
    def __init__(self, ability_name: str, minimum_damage: int, maximum_damage: int):
        self.ability_name = ability_name
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage

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

class CharacterEquipment:
    def __init__(self, weapon: Weapon = None, armour: Armour = None):
        self.weapon = weapon
        self.armour = armour

class Character:
    def __init__(self, name: str, health_points: int, level: int, armour_class: int, abilities: list[Ability], equipment: CharacterEquipment = None, inventory: list[Item] = None):
        self.name = name
        self.health_points = health_points
        self.max_health_points = health_points
        self.level = level
        self.armour_class = armour_class
        self.equipment = equipment
        self.inventory = inventory
        self.abilities = abilities
        self.current_experience = 0
        self.experience_to_next_level = self.level * 10

        if inventory is None:
            self.inventory = []

    def attack(self, target: 'Character', ability: Ability):
        if dice.roll() > target.armour_class:
            weapon_bonus = 0
            if self.equipment and self.equipment.weapon:
                weapon_bonus = self.equipment.weapon.damage_bonus

            attack_damage = (dice.roll(ability.minimum_damage, ability.maximum_damage) + weapon_bonus) * self.level
            target.health_points -= attack_damage
            print(f"{self.name} attacked {target.name} with {ability.ability_name} for {attack_damage} damage")
        else:
            print(f"{self.name} attacked {target.name} with {ability.ability_name}, but missed")

    def is_defeated(self) -> bool:
        return self.health_points <= 0

    def calculate_experience_points(self):
        return self.max_health_points * self.level

    def level_up(self):
        self.current_experience = self.current_experience - self.experience_to_next_level
        self.level += 1
        self.experience_to_next_level = self.level * 10
        self.max_health_points += 6

class Dice:
    def __init__(self):
        random.seed()

    def roll(self, min: int=1, max: int=20) -> int:
        return random.randrange(min, max + 1)

    def choose_index(self, max: int) -> int:
        return random.randrange(max)

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

player_abilities = [Ability("Advanced attack", 4, 6), Ability("Basic attack", 2, 3)]
starter_weapon = Weapon("Starter sword", damage_bonus=1)
player_equipment = CharacterEquipment(weapon=starter_weapon)
player = Character("Player", health_points=10, level=1, armour_class=15, equipment=player_equipment, abilities=player_abilities)

rat_abilities = [Ability("Bite", 2, 3), Ability("Screech", 1, 2)]
rat1 = Character("Rat 1", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
rat2 = Character("Rat 2", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
rat_room = Room([rat1, rat2])

rat_boss = Character("Rat boss", health_points=20, level=2, armour_class=12, abilities=rat_abilities)
longsword = Weapon("Longsword", 2)
health_potion = Item("Health potion")
rat_boss_room = Room([rat_boss], [longsword, health_potion])

gelatinous_cube_abilities = [Ability("Ooze", 3, 6), Ability("Engulf", 7, 10)]
gelatinous_cube = Character("Gelatinous cube", 84, 1, 8, gelatinous_cube_abilities)
gelatinous_armour = Armour("Gelatinous armour", 18)
gelatinous_cube_room = Room([gelatinous_cube], [gelatinous_armour])

displacer_beast_abilities = [Ability("Multiattack", 10, 16), Ability("Tentacle attack", 8, 18)]
displacer_beast = Character("Displacer beast", 85, 1, 13, displacer_beast_abilities)
displacer_beast_room = Room([displacer_beast])

spectator_abilities = [Ability("Wounding ray", 10, 25), Ability("Fear ray", 10, 20), Ability("Bite", 12, 20)]
spectator = Character("Spectator", 39, 1, 14, spectator_abilities)
spectator_room = Room([spectator])

wyrmling_abilities = [Ability("Poison breath", 10, 21), Ability("Bite", 7, 10)]
wyrmling1 = Character("Green dragon wyrmling 1", 38, 1, 17, wyrmling_abilities)
wyrmling2 = Character("Green dragon wyrmling 2", 38, 1, 17, wyrmling_abilities)
wyrmling3 = Character("Green dragon wyrmling 3", 38, 1, 17, wyrmling_abilities)
wyrmling_room = Room([wyrmling1, wyrmling2, wyrmling3])

wyrmling4 = Character("Green dragon wyrmling 4", 38, 6, 17, wyrmling_abilities)
dragon_abilities = [Ability("Poison breath", 28, 56), Ability("Bite", 17, 26), Ability("Claw", 13, 18), Ability("Tail", 15, 22), Ability("Frightful presence", 20, 25)]
green_dragon = Character("Green dragon", 207, 7, 19, dragon_abilities)
dragon_room = Room([green_dragon, wyrmling4])

dungeon = Dungeon([rat_room, rat_boss_room, gelatinous_cube_room, displacer_beast_room, spectator_room, wyrmling_room, dragon_room])

dice = Dice()

for number, room in enumerate(dungeon.rooms, start=1):
    if player.is_defeated():
        break

    print("Room", number)
    while room.has_enemies():
        print("New turn. Health status:")
        for participant in [player] + room.enemies:
            print(f"{participant.name}: {participant.health_points}/{participant.max_health_points} health points")
        
        enemy_to_attack = room.enemies[0]
        ability_to_use = player.abilities[dice.choose_index(len(player_abilities))]
        player.attack(enemy_to_attack, ability_to_use)
        
        if enemy_to_attack.is_defeated():
            room.enemies.remove(enemy_to_attack)
            print(enemy_to_attack.name, "was defeated!")
            experience = enemy_to_attack.calculate_experience_points()
            player.current_experience += experience
            print(player.name, "gained", experience, "experience points.")

            if player.current_experience >= player.experience_to_next_level:
                player.level_up()
                print("Player levelled up! Player is now level", player.level)
            
            print(f"Experience status: Level {player.level}. {player.current_experience}/{player.experience_to_next_level} experience points to level up.")
        
        for enemy in room.enemies:
            ability_to_use = enemy.abilities[dice.choose_index(len(enemy.abilities))]
            enemy.attack(player, ability_to_use)

        if not room.has_enemies():
            print("Enemies defeated!")
            player.health_points = player.max_health_points
            print(player.name, "rested and regained their health points.")

            if hasattr(room, "items"):
                for item in room.items:
                    if isinstance(item, Weapon):
                        if player.equipment.weapon:
                            player.inventory.append(player.equipment.weapon)
                        player.equipment.weapon = item
                        print(player.name, "found and equipped weapon", item.name)

                    elif isinstance(item, Armour):
                        if player.equipment.armour:
                            player.inventory.append(player.equipment.armour)
                        player.equipment.armour = item
                        player.armour_class = item.armour_class
                        print(player.name, "found and equipped armour", item.name)

                    else:
                        player.inventory.append(item)
                        print(player.name, "found", item.name, "and put it in their inventory.")
                    
        elif player.is_defeated():
            print(player.name, "was defeated. Game over!")
            break

        print("\n")