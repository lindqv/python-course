from characters import Ability, CharacterEquipment, Character
from items import Weapon

player_abilities = [Ability("Advanced attack", 4, 6), Ability("Basic attack", 2, 3)]
starter_weapon = Weapon("Starter sword", damage_bonus=1)
player_equipment = CharacterEquipment(weapon=starter_weapon)
default_player = Character("Player", health_points=10, level=1, armour_class=15, equipment=player_equipment, abilities=player_abilities)