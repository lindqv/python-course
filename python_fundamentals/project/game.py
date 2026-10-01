from items import Dice
from dungeon_data import dungeon
from player_data import default_player
from quest_data import default_quests
from quests import QuestLog
from combat import Combat
from user_input import choose_action_after_combat

class Game:
    def __init__(self, interactive=True):
        self.dice = Dice()
        self.combat = Combat(self.dice, interactive)
        self.player = default_player
        self.dungeon = dungeon
        self.quest_log = QuestLog(default_quests)
        self.interactive = interactive

    def play(self):
        for room_number, room in enumerate(self.dungeon.rooms, start=1):
            print("Room", room_number)
            self.quest_log.update_quests(self.combat.statistics.get("enemies_defeated", 0), room_number)
            if room.has_enemies():
                self.combat.start(room.enemies, self.player)  

            if self.player.is_defeated():
                break       

            if self.interactive:
                choose_action_after_combat(self.player, room)
            else:
                self.player.loot(room.items)
                self.player.rest()

            self.quest_log.update_quests(self.combat.statistics.get("enemies_defeated", 0), room_number)
            self.quest_log.show_status()

        print("The adventure ends.")
        self.quest_log.show_status()
        self.show_statistics()

    def show_statistics(self):
        player_attacks = self.player.statistics.get("attacks", 0)
        player_hits = self.player.statistics.get("hits", 0)
        player_hit_rate = (player_hits / player_attacks) * 100

        print("\n")
        print("Adventure statistics:")
        print("Enemy attacks:", self.combat.statistics.get("enemy_attacks", 0))
        print("Enemies defeated:", self.combat.statistics.get("enemies_defeated", 0))
        print("Player attacks:", player_attacks)
        print("Player hits:", player_hits)
        print(f"Player hit rate: {player_hit_rate:.1f} %")

