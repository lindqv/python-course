from items import Dice
from dungeon_data import dungeon
from player_data import default_player
from combat import Combat
from user_input import choose_action_after_combat

class Game:
    def __init__(self, interactive=True):
        self.dice = Dice()
        self.combat = Combat(self.dice, interactive)
        self.player = default_player
        self.dungeon = dungeon
        self.interactive = interactive

    def play(self):
        for number, room in enumerate(self.dungeon.rooms, start=1):
            print("Room", number)
            if room.has_enemies():
                self.combat.start(room.enemies, self.player)  

            if self.player.is_defeated():
                break       

            if self.interactive:
                choose_action_after_combat(self.player, room)
            else:
                self.player.loot(room.items)
                self.player.rest()

