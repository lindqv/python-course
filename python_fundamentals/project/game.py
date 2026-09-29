from items import Dice
from dungeon import Room
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

    def choose_action(self, room: Room):
        actions = ["Attack", "Skip turn"]
        choice = self.choose(actions, "What would you like to do?")

        if choice == "Attack":
            enemy_to_attack = self.choose(room.enemies, "Which enemy would you like to attack?")
            ability = self.choose(self.player.abilities, "Which ability would you like to use?")
            self.player.attack(enemy_to_attack, ability, self.dice)

            if enemy_to_attack.is_defeated():
                room.enemies.remove(enemy_to_attack)
                print(enemy_to_attack.name, "was defeated!")
                experience = enemy_to_attack.calculate_experience_points()
                self.player.gain_experience_points(experience)
        else:
            return

    def choose(self, options: list, question: str):
        if len(options) == 1:
            return options[0]
        else:
            print(question)
            for number, option in enumerate(options, start=1):
                print(f"{number}. {option}")
        
        choice = self.choose_integer(1, len(options))
        chosen_index = choice - 1
        return options[chosen_index]

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
                    
        
