from items import Dice
from dungeon_data import dungeon
from player_data import default_player

dice = Dice()
player = default_player

for number, room in enumerate(dungeon.rooms, start=1):
    if player.is_defeated():
        break

    print("Room", number)
    while room.has_enemies():
        print("New turn. Health status:")
        for participant in [player] + room.enemies:
            print(f"{participant.name}: {participant.health_points}/{participant.max_health_points} health points")
        
        enemy_to_attack = room.enemies[0]
        ability_to_use = player.abilities[dice.choose_index(len(player.abilities))]
        player.attack(enemy_to_attack, ability_to_use, dice)
        
        if enemy_to_attack.is_defeated():
            room.enemies.remove(enemy_to_attack)
            print(enemy_to_attack.name, "was defeated!")
            experience = enemy_to_attack.calculate_experience_points()
            player.gain_experience_points(experience)
        
        for enemy in room.enemies:
            ability_to_use = enemy.abilities[dice.choose_index(len(enemy.abilities))]
            enemy.attack(player, ability_to_use, dice)

        if player.is_defeated():
            print(player.name, "was defeated. Game over!")
            break

        print("\n")                    

    if not room.has_enemies():
        player.rest()
        player.loot(room.items)