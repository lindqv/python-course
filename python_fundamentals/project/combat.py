from characters import Player, Enemy
from user_input import choose_action_in_combat
from items import Dice

class Combat:
    def __init__(self, dice: Dice, interactive=True):
        self.dice = dice
        self.interactive = interactive

    def start(self, enemies: list[Enemy], player: Player):
        print("Combat started!")
        while enemies:
            print("New turn. Health status:")
            for participant in [player] + enemies:
                print(f"    {participant.name}: {participant.health_points}/{participant.max_health_points} health points")
        
            if self.interactive:
                choose_action_in_combat(enemies, player, self.dice)
            else:
                self.automatic_attack(enemies, player)
        
            self.handle_defeated_enemies(enemies, player)
        
            for enemy in enemies:
                ability_to_use = enemy.abilities[self.dice.choose_index(len(enemy.abilities))]
                enemy.attack(player, ability_to_use, self.dice)
        
            if player.is_defeated():
                print(player.name, "was defeated. Game over!")
                break
        
            print("\n")

        print("Combat ended.")

    def automatic_attack(self, enemies: list[Enemy], player: Player):
        enemy_to_attack = enemies[0]
        ability_to_use = player.abilities[self.dice.choose_index(len(player.abilities))]
        player.attack(enemy_to_attack, ability_to_use, self.dice)
    
    def handle_defeated_enemies(self, enemies: list[Enemy], player: Player):
        for enemy in enemies:
            if enemy.is_defeated():
                enemies.remove(enemy)
                print(enemy.name, "was defeated!")
                experience = enemy.calculate_experience_points()
                player.gain_experience_points(experience)