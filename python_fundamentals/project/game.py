from items import Dice
from dungeon_data import dungeon
from player_data import default_player

class Game:
    def __init__(self):
        self.dice = Dice()
        self.player = default_player

    def automatic_mode(self):
        for number, room in enumerate(dungeon.rooms, start=1):
            if self.player.is_defeated():
                break

            print("Room", number)
            while room.has_enemies():
                print("New turn. Health status:")
                for participant in [self.player] + room.enemies:
                    print(f"{participant.name}: {participant.health_points}/{participant.max_health_points} health points")
        
                enemy_to_attack = room.enemies[0]
                ability_to_use = self.player.abilities[self.dice.choose_index(len(self.player.abilities))]
                self.player.attack(enemy_to_attack, ability_to_use, self.dice)
        
                if enemy_to_attack.is_defeated():
                    room.enemies.remove(enemy_to_attack)
                    print(enemy_to_attack.name, "was defeated!")
                    experience = enemy_to_attack.calculate_experience_points()
                    self.player.gain_experience_points(experience)
        
                for enemy in room.enemies:
                    ability_to_use = enemy.abilities[self.dice.choose_index(len(enemy.abilities))]
                    enemy.attack(self.player, ability_to_use, self.dice)

                if self.player.is_defeated():
                    print(self.player.name, "was defeated. Game over!")
                    break

                print("\n")                    

        if not room.has_enemies():
            self.player.rest()
            self.player.loot(room.items)

    def interactive_mode(self):
        for number, room in enumerate(dungeon.rooms, start=1):
            if self.player.is_defeated():
                break

            print("Room", number)
            while room.has_enemies():
                print("New turn. Health status:")
                for participant in [self.player] + room.enemies:
                    print(f"{participant.name}: {participant.health_points}/{participant.max_health_points} health points")

                self.choose_action(room)

                for enemy in room.enemies:
                    ability_to_use = enemy.abilities[self.dice.choose_index(len(enemy.abilities))]
                    enemy.attack(self.player, ability_to_use, self.dice)

                if self.player.is_defeated():
                    print(self.player.name, "was defeated. Game over!")
                    break

                print("\n")                    

        if not room.has_enemies():
            self.player.rest()
            self.player.loot(room.items)

    def choose_integer(self, min: int, max: int):
        user_input = input(f"Make a choice by typing an integer between {min} and {max}: ").strip()
        try:
            choice = int(user_input)
            if choice < min or choice > max:
                print("Choice out of range, try again.")
                self.choose_integer(min, max)
            else:
                return choice
        except:
            print("Invalid choice, try again.")
            self.choose_integer(min, max)
        

    def choose_action(self, room):
        print("What would you like to do?")
        print("1. Attack")
        print("2. Skip turn")
        
        choice = self.choose_integer(1,2)

        if choice == 1:
            enemy_to_attack = self.choose_enemy_to_attack(room.enemies)
            ability = self.choose_ability(self.player.abilities)
            self.attack(enemy_to_attack, ability, room)
        else:
            return

    def choose_enemy_to_attack(self, enemies):
        if len(enemies) == 1:
            return enemies[0]
        else:
            print("Which enemy would you like to attack?")
            for number, enemy in enumerate(enemies, start=1):
                print(f"{number}. {enemy.name}")

        choice = self.choose_integer(1, len(enemies))
        chosen_index = choice - 1
        return enemies[chosen_index]

    def choose_ability(self, abilities):
            if len(abilities) == 1:
                return abilities[0]
            else:
                print("Which ability would you like to use?")
                for number, ability in enumerate(abilities, start=1):
                    print(f"{number}. {ability}")
    
            choice = self.choose_integer(1, len(abilities))
            chosen_index = choice - 1
            return abilities[chosen_index]

    def attack(self, enemy_to_attack, ability_to_use, room):
        self.player.attack(enemy_to_attack, ability_to_use, self.dice)
                    
        if enemy_to_attack.is_defeated():
            room.enemies.remove(enemy_to_attack)
            print(enemy_to_attack.name, "was defeated!")
            experience = enemy_to_attack.calculate_experience_points()
            self.player.gain_experience_points(experience)

    def use_item(self):
        return
