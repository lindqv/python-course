from items import Dice
from dungeon_data import dungeon
from player_data import default_player
from user_input import choose_action
from characters import Character

class Game:
    def __init__(self, interactive=True):
        self.dice = Dice()
        self.player = default_player
        self.dungeon = dungeon
        self.interactive = interactive

    def play(self):
        for number, room in enumerate(self.dungeon.rooms, start=1):
            if self.player.is_defeated():
                break

            print("Room", number)
            print("Combat started!")
            while room.has_enemies():
                print("New turn. Health status:")
                for participant in [self.player] + room.enemies:
                    print(f"    {participant.name}: {participant.health_points}/{participant.max_health_points} health points")

                if self.interactive:
                    choose_action(room, self.player, self.dice)
                else:
                    self.automatic_attack(room.enemies)

                self.handle_defeated_enemies(room.enemies, self.player)

                for enemy in room.enemies:
                    ability_to_use = enemy.abilities[self.dice.choose_index(len(enemy.abilities))]
                    enemy.attack(self.player, ability_to_use, self.dice)

                if self.player.is_defeated():
                    print(self.player.name, "was defeated. Game over!")
                    break

                print("\n")                    

            if not room.has_enemies():
                print("Combat ended.")
                self.player.rest()
                self.player.loot(room.items)

    def automatic_attack(self, enemies: list[Character]):
        enemy_to_attack = enemies[0]
        ability_to_use = self.player.abilities[self.dice.choose_index(len(self.player.abilities))]
        self.player.attack(enemy_to_attack, ability_to_use, self.dice)

    def handle_defeated_enemies(self, enemies: list[Character], player: Character):
        for enemy in enemies:
            if enemy.is_defeated():
                enemies.remove(enemy)
                print(enemy.name, "was defeated!")
                experience = enemy.calculate_experience_points()
                player.gain_experience_points(experience)

