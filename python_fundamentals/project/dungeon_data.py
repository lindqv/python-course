from characters import Ability, Enemy
from items import HealthPotion, Armour, Weapon
from dungeon import Room, Dungeon

rat_abilities = [Ability("Bite", 2, 3), Ability("Screech", 1, 2)]
rat1 = Enemy("Rat 1", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
rat2 = Enemy("Rat 2", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
rat_room = Room([rat1, rat2])

rat_boss = Enemy("Rat boss", health_points=20, level=2, armour_class=12, abilities=rat_abilities)
longsword = Weapon("Longsword", 7)
health_potion = HealthPotion("Large health potion", 10)
rat_boss_room = Room([rat_boss], [longsword, health_potion])

gelatinous_cube_abilities = [Ability("Ooze", 3, 6), Ability("Engulf", 7, 10)]
gelatinous_cube = Enemy("Gelatinous cube", health_points=50, level=3, armour_class=8, abilities=gelatinous_cube_abilities)
gelatinous_armour = Armour("Gelatinous armour", 18)
gelatinous_cube_room = Room([gelatinous_cube], [gelatinous_armour])

displacer_beast_abilities = [Ability("Multiattack", 10, 16), Ability("Tentacle attack", 8, 18)]
displacer_beast = Enemy("Displacer beast", health_points=85, level=4, armour_class=13, abilities=displacer_beast_abilities)
displacer_beast_room = Room([displacer_beast])

greatsword = Weapon("Greatsword", 10)
spectator_abilities = [Ability("Wounding ray", 10, 25), Ability("Fear ray", 10, 20), Ability("Bite", 12, 20)]
spectator = Enemy("Spectator", health_points=39, level=5, armour_class=14, abilities=spectator_abilities)
spectator_room = Room([spectator], [greatsword])

wyrmling_abilities = [Ability("Poison breath", 3, 5), Ability("Bite", 7, 10)]
wyrmling1 = Enemy("Green dragon wyrmling 1", health_points=38, level=4, armour_class=16, abilities=wyrmling_abilities)
wyrmling2 = Enemy("Green dragon wyrmling 2", health_points=38, level=4, armour_class=16, abilities=wyrmling_abilities)
wyrmling3 = Enemy("Green dragon wyrmling 3", health_points=38, level=4, armour_class=16, abilities=wyrmling_abilities)
wyrmling_room = Room([wyrmling1, wyrmling2, wyrmling3])

dragon_abilities = [Ability("Poison breath", 20, 25), Ability("Bite", 15, 19), Ability("Claw", 13, 18), Ability("Tail", 13, 17), Ability("Frightful presence", 12, 15)]
green_dragon = Enemy("Green dragon", health_points=207, level=7, armour_class=17, abilities=dragon_abilities)
dragon_room = Room([green_dragon])

dungeon = Dungeon([rat_room, rat_boss_room, gelatinous_cube_room, spectator_room, displacer_beast_room, wyrmling_room, dragon_room])