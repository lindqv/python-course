from items import Item, Weapon, Armour, Dice

class Ability:
    def __init__(self, ability_name: str, minimum_damage: int, maximum_damage: int):
        self.ability_name = ability_name
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage

    def __str__(self):
        return self.ability_name

class CharacterEquipment:
    def __init__(self, weapon: Weapon = None, armour: Armour = None):
        self.weapon = weapon
        self.armour = armour

class Character:
    def __init__(self, name: str, health_points: int, level: int, armour_class: int, abilities: list[Ability], 
                 equipment: CharacterEquipment = None, inventory: list[Item] = None):
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

    def __str__(self):
        return f"{self.name}, {self.health_points}/{self.max_health_points} health points"

    def attack(self, target: 'Character', ability: Ability, dice: Dice):
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
    
class Enemy(Character):
    def __init__(self, name, health_points, level, armour_class, abilities, equipment = None, inventory = None):
        super().__init__(name, health_points, level, armour_class, abilities, equipment, inventory)

    def calculate_experience_points(self):
        return self.max_health_points * self.level

class Player(Character):
    def __init__(self, name, health_points, level, armour_class, abilities, equipment = None, inventory = None):
        super().__init__(name, health_points, level, armour_class, abilities, equipment, inventory)

    def level_up(self):
        self.current_experience = self.current_experience - self.experience_to_next_level
        self.level += 1
        self.experience_to_next_level = self.level * 10
        self.max_health_points += 6

    def gain_experience_points(self, experience: int):
        self.current_experience += experience
        print(self.name, "gained", experience, "experience points.")
        
        while self.current_experience >= self.experience_to_next_level:
            self.level_up()
            print("Player levelled up! Player is now level", self.level)
                    
        print(f"Experience status: Level {self.level}. {self.current_experience}/{self.experience_to_next_level} experience points to level up.")
    
    def equip_weapon(self, new_weapon: Weapon):
        current_weapon = self.equipment.weapon
        if current_weapon:
            self.inventory.append(current_weapon)

        self.equipment.weapon = new_weapon

    def equip_armour(self, new_armour: Armour):
        current_armour = self.equipment.armour
        if current_armour:
            self.inventory.append(current_armour)
    
        self.equipment.armour = new_armour
        self.armour_class = new_armour.armour_class

    def loot(self, items: list[Item]):
        if len(items) == 0:
            print("There is nothing to loot.")

        for item in items:
            if isinstance(item, Weapon):
                self.equip_weapon(item)
                print(f"{self.name} found and equipped weapon {item.name}.")
            
            elif isinstance(item, Armour):
                self.equip_armour(item)
                print(f"{self.name} found and equipped armour {item.name}.")
            
            else:
                self.inventory.append(item)
                print(f"{self.name} found {item.name} and put it in their inventory.")
    
    def rest(self):
        self.health_points = self.max_health_points
        print(self.name, "rested and regained their health points.")

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("The inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(item)