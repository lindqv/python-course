from characters import Ability, CharacterEquipment, Player
from items import Weapon, HealthPotion

player_abilities = [Ability("Main hand attack", minimum_damage=2, maximum_damage=3), 
                    Ability("Thunderous smite", minimum_damage=4, maximum_damage=6, has_limited_uses=True, limited_uses=2)]
starter_weapon = Weapon("Starter sword", damage_bonus=5)
player_equipment = CharacterEquipment(weapon=starter_weapon)
player_inventory = [HealthPotion("Small health potion", 5), HealthPotion("Large health potion", 10)]
default_player = Player("Player", health_points=12, level=1, armour_class=15, equipment=player_equipment, 
                        abilities=player_abilities, inventory=player_inventory)