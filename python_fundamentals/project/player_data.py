from characters import Ability, CharacterEquipment, Player
from items import Weapon, HealthPotion

player_abilities = [Ability("Advanced attack", 4, 6), Ability("Basic attack", 2, 3)]
starter_weapon = Weapon("Starter sword", damage_bonus=5)
player_equipment = CharacterEquipment(weapon=starter_weapon)
player_inventory = [HealthPotion("Small health potion", 5), HealthPotion("Large health potion", 10)]
default_player = Player("Player", health_points=12, level=1, armour_class=15, equipment=player_equipment, 
                        abilities=player_abilities, inventory=player_inventory)