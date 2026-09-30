from characters import Ability, Enemy
from items import Item, Armour, Weapon
from dungeon import Room, Dungeon

rat_abilities = [Ability("Bite", 2, 3), Ability("Screech", 1, 2)]
rat1 = Enemy("Rat 1", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
rat2 = Enemy("Rat 2", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
rat_room = Room([rat1, rat2])

rat_boss = Enemy("Rat boss", health_points=20, level=2, armour_class=12, abilities=rat_abilities)
longsword = Weapon("Longsword", 2)
health_potion = Item("Health potion")
rat_boss_room = Room([rat_boss], [longsword, health_potion])

gelatinous_cube_abilities = [Ability("Ooze", 3, 6), Ability("Engulf", 7, 10)]
gelatinous_cube = Enemy("Gelatinous cube", 84, 1, 8, gelatinous_cube_abilities)
gelatinous_armour = Armour("Gelatinous armour", 18)
gelatinous_cube_room = Room([gelatinous_cube], [gelatinous_armour])

displacer_beast_abilities = [Ability("Multiattack", 10, 16), Ability("Tentacle attack", 8, 18)]
displacer_beast = Enemy("Displacer beast", 85, 1, 13, displacer_beast_abilities)
displacer_beast_room = Room([displacer_beast])

spectator_abilities = [Ability("Wounding ray", 10, 25), Ability("Fear ray", 10, 20), Ability("Bite", 12, 20)]
spectator = Enemy("Spectator", 39, 1, 14, spectator_abilities)
spectator_room = Room([spectator])

wyrmling_abilities = [Ability("Poison breath", 10, 21), Ability("Bite", 7, 10)]
wyrmling1 = Enemy("Green dragon wyrmling 1", 38, 1, 17, wyrmling_abilities)
wyrmling2 = Enemy("Green dragon wyrmling 2", 38, 1, 17, wyrmling_abilities)
wyrmling3 = Enemy("Green dragon wyrmling 3", 38, 1, 17, wyrmling_abilities)
wyrmling_room = Room([wyrmling1, wyrmling2, wyrmling3])

wyrmling4 = Enemy("Green dragon wyrmling 4", 38, 6, 17, wyrmling_abilities)
dragon_abilities = [Ability("Poison breath", 28, 56), Ability("Bite", 17, 26), Ability("Claw", 13, 18), Ability("Tail", 15, 22), Ability("Frightful presence", 20, 25)]
green_dragon = Enemy("Green dragon", 207, 7, 19, dragon_abilities)
dragon_room = Room([green_dragon, wyrmling4])

dungeon = Dungeon([rat_room, rat_boss_room, gelatinous_cube_room, displacer_beast_room, spectator_room, wyrmling_room, dragon_room])