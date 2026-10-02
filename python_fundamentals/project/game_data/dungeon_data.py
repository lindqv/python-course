from characters import Ability, Enemy
from items import HealthPotion, Armour, Item, Weapon
from dungeon import Room, Dungeon

rat_abilities = [Ability("Bite", minimum_damage=2, maximum_damage=3), 
                 Ability("Screech", minimum_damage=1, maximum_damage=2)]
rat1 = Enemy("Rat 1", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
rat2 = Enemy("Rat 2", health_points=5, level=1, armour_class=8, abilities=rat_abilities)
coin = Item("Gold coin")
rat_room = Room([rat1, rat2], [coin])

rat_boss = Enemy("Rat boss", health_points=20, level=2, armour_class=12, abilities=rat_abilities)
longsword = Weapon("Longsword", damage_bonus=7)
health_potion = HealthPotion("Large health potion", healing=10)
rat_boss_room = Room([rat_boss], [longsword, health_potion])

gelatinous_cube_abilities = [Ability("Ooze", minimum_damage=3, maximum_damage=6), 
                             Ability("Engulf", minimum_damage=7, maximum_damage=10)]
gelatinous_cube = Enemy("Gelatinous cube", health_points=50, level=3, armour_class=8, abilities=gelatinous_cube_abilities)
gelatinous_armour = Armour("Gelatinous armour", armour_class=16)
jelly_cake = Item("Green jelly cake")
gelatinous_cube_room = Room([gelatinous_cube], [gelatinous_armour, jelly_cake])

displacer_beast_abilities = [Ability("Multiattack", minimum_damage=10, maximum_damage=16), 
                             Ability("Tentacle attack", minimum_damage=8, maximum_damage=18)]
displacer_beast = Enemy("Displacer beast", health_points=85, level=4, armour_class=13, abilities=displacer_beast_abilities)
health_potion_xl = HealthPotion("Extra large health potion", healing=20)
displacer_beast_room = Room([displacer_beast], [health_potion_xl])

spectator_abilities = [Ability("Wounding ray", minimum_damage=10, maximum_damage=25), 
                       Ability("Fear ray", minimum_damage=10, maximum_damage=20), 
                       Ability("Bite", minimum_damage=12, maximum_damage=20)]
spectator = Enemy("Spectator", health_points=39, level=5, armour_class=14, abilities=spectator_abilities)
greatsword = Weapon("Greatsword", damage_bonus=10)
spectator_room = Room([spectator], [greatsword])

wyrmling_abilities = [Ability("Poison breath", minimum_damage=3, maximum_damage=5), 
                      Ability("Bite", minimum_damage=7, maximum_damage=10)]
wyrmling1 = Enemy("Green dragon wyrmling 1", health_points=38, level=4, armour_class=16, abilities=wyrmling_abilities)
wyrmling2 = Enemy("Green dragon wyrmling 2", health_points=38, level=4, armour_class=16, abilities=wyrmling_abilities)
wyrmling3 = Enemy("Green dragon wyrmling 3", health_points=38, level=4, armour_class=16, abilities=wyrmling_abilities)
dragonscale_armour = Armour("Dragonscale armour", armour_class=18)
emerald = Item("Emerald")
new_health_potion_xl = HealthPotion("Extra large health potion", healing=20)
wyrmling_room = Room([wyrmling1, wyrmling2, wyrmling3], [dragonscale_armour, emerald, new_health_potion_xl])

dragon_abilities = [Ability("Poison breath", minimum_damage=20, maximum_damage=25), 
                    Ability("Bite", minimum_damage=15, maximum_damage=19), 
                    Ability("Claw", minimum_damage=13, maximum_damage=18), 
                    Ability("Tail", minimum_damage=13, maximum_damage=17), 
                    Ability("Frightful presence", minimum_damage=12, maximum_damage=15)]
green_dragon = Enemy("Green dragon", health_points=207, level=2, armour_class=17, abilities=dragon_abilities)
dragonslayer_blade = Weapon("Dragonslayer blade", damage_bonus=15)
gold = Item("Large sack of gold")
poison = Item("Vial of green poison")
jewels = Item("A large collection of jewels")
dragon_room = Room([green_dragon], [dragonslayer_blade, gold, poison, jewels])

dungeon = Dungeon([rat_room, rat_boss_room, gelatinous_cube_room, spectator_room, displacer_beast_room, wyrmling_room, dragon_room])