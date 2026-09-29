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