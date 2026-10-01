from items import Item, Weapon, Armour, Dice

class Ability:
    def __init__(self, ability_name: str, minimum_damage: int, maximum_damage: int, has_limited_uses: bool = False, limited_uses: int | None = None):
        self.ability_name = ability_name
        self.minimum_damage = minimum_damage
        self.maximum_damage = maximum_damage
        self.has_limited_uses = has_limited_uses
        self.limited_uses = limited_uses
        self.maximum_limited_uses = limited_uses

    def __str__(self):
        if self.has_limited_uses:
            return f"{self.ability_name}, {self.limited_uses}/{self.maximum_limited_uses} uses left"
        return self.ability_name

class CharacterEquipment:
    def __init__(self, weapon: Weapon = None, armour: Armour = None):
        self.weapon = weapon
        self.armour = armour

    def __str__(self):
        return f"Weapon: {self.weapon.__str__()}, Armour: {self.armour.__str__()}"

class Character:
    def __init__(self, name: str, health_points: int, level: int, armour_class: int, abilities: list[Ability], 
                 equipment: CharacterEquipment = None, inventory: list[Item] = None, hit_bonus=5):
        self.name = name
        self.health_points = health_points
        self.max_health_points = health_points
        self.level = level
        self.armour_class = armour_class
        self.equipment = equipment
        self.inventory = inventory
        self.abilities = abilities
        self.hit_bonus = hit_bonus
        self.current_experience = 0
        self.experience_to_next_level = self.level * 10
        self.statistics = {
            "attacks": 0,
            "hits": 0,
        }

        if inventory is None:
            self.inventory = []

    def __str__(self):
        return f"{self.name}, {self.health_points}/{self.max_health_points} health points"

    def attack(self, target: 'Character', ability: Ability, dice: Dice):
        self.statistics["attacks"] += 1
        if dice.roll() + self.hit_bonus > target.armour_class:
            self.statistics["hits"] += 1
            weapon_bonus = 0
            if self.equipment and self.equipment.weapon:
                weapon_bonus = self.equipment.weapon.damage_bonus

            attack_damage = (dice.roll(ability.minimum_damage, ability.maximum_damage) + weapon_bonus)
            target.health_points -= attack_damage
            if ability.has_limited_uses:
                ability.limited_uses -= 1
            print(f"{self.name} attacked {target.name} with {ability.ability_name} for {attack_damage} damage")
        else:
            print(f"{self.name} attacked {target.name} with {ability.ability_name}, but missed")

    def is_defeated(self) -> bool:
        return self.health_points <= 0

    def get_available_abilities(self):
        available_abilities = []
        for ability in self.abilities:
            if ability.has_limited_uses:
                if ability.limited_uses >= 1:
                    available_abilities.append(ability)
            else:
                available_abilities.append(ability)
        return available_abilities

    def reset_limited_use_abilities(self):
        for ability in self.abilities:
            if ability.has_limited_uses:
                ability.limited_uses = ability.maximum_limited_uses
    
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

        for ability in self.abilities:
            ability.minimum_damage += 1
            ability.maximum_damage += 1

    def gain_experience_points(self, experience: int):
        self.current_experience += experience
        print(self.name, "gained", experience, "experience points.")
        
        while self.current_experience >= self.experience_to_next_level:
            self.level_up()
            print("Player levelled up! Player is now level", self.level)

        self.show_experience_status()           
    
    def equip_weapon(self, new_weapon: Weapon):
        current_weapon = self.equipment.weapon
        if current_weapon:
            self.inventory.append(current_weapon)
            print(self.name, "placed", current_weapon, "in their inventory")
        if new_weapon in self.inventory:
            self.inventory.remove(new_weapon)

        self.equipment.weapon = new_weapon
        print(f"{self.name} is now using {self.equipment.weapon}.")

    def equip_armour(self, new_armour: Armour):
        current_armour = self.equipment.armour
        if current_armour:
            self.inventory.append(current_armour)
            print(self.name, "placed", current_armour, "in their inventory")
        if new_armour in self.inventory:
            self.inventory.remove(new_armour)
    
        self.equipment.armour = new_armour
        self.armour_class = new_armour.armour_class
        print(f"{self.name} is now using {self.equipment.armour}")

    def loot(self, items: list[Item]):
        if len(items) == 0:
            print("There is nothing to loot.")
            return

        for item in items:
            if isinstance(item, Weapon):
                print(f"{self.name} found and equipped weapon {item.name}.")
                self.equip_weapon(item)
                    
            elif isinstance(item, Armour):
                print(f"{self.name} found and equipped armour {item.name}.")
                self.equip_armour(item)
                    
            else:
                print(f"{self.name} found {item.name} and put it in their inventory.")
                self.inventory.append(item)

        items.clear()
    
    def rest(self):
        self.health_points = self.max_health_points
        self.reset_limited_use_abilities()
        print(self.name, "rested and regained their health points and ability uses.")

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("The inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print(item)

    def show_equipment(self):
        print(self.equipment)

    def show_experience_status(self):
        print(f"Experience status: Level {self.level}. {self.current_experience}/{self.experience_to_next_level} experience points to level up.")

    def show_player_status(self):
        print(f"{self.health_points}/{self.max_health_points} health points")
