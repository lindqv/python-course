from characters import Player, Enemy
from items import Dice, Item
from dungeon import Room

def choose_action_in_combat(enemies: list[Enemy], player: Player, dice: Dice):
    actions = ["Attack", "Use or equip item", "Skip turn"]
    choice = choose(actions, "What would you like to do?")

    if choice == "Attack":
        enemy_to_attack = choose(enemies, "Which enemy would you like to attack?")
        available_abilities = player.get_available_abilities()
        ability = choose(available_abilities, "Which ability would you like to use?")
        player.attack(enemy_to_attack, ability, dice)
    elif choice == "Use or equip item":
        chosen_item = choose_item(player)
        if chosen_item:
            chosen_item.use(player)
    else:
        return

def choose_action_after_combat(player: Player, room: Room):
    choice = ""
    choices = ["Loot", "Rest", "Show player status", "Show experience status", "Show equipment", 
               "Show inventory", "Use or equip item", "Go to next room"]
    while choice != "Go to next room":
        choice = choose(choices, "What would you like to do?")
        if choice == "Loot":
            player.loot(room.items)
        elif choice == "Rest":
            player.rest()
        elif choice == "Show player status":
            player.show_player_status()
        elif choice == "Show experience status":
            player.show_experience_status()
        elif choice == "Show equipment":
            player.show_equipment()
        elif choice == "Show inventory":
            player.show_inventory()
        elif choice == "Use or equip item":
            chosen_item = choose_item(player)
            if chosen_item:
                chosen_item.use(player)

def choose_item(player: Player) -> Item | None:
    player.show_inventory()
    options = player.inventory + ["Go back"]
    choice = choose(options, "Which item would you like to use or equip? Or choose 'Go back' to return.")
    if choice != "Go back":
        return choice
        
def choose(options: list, question: str):
    if len(options) == 1:
        return options[0]
    else:
        print("\n" + question)
        for number, option in enumerate(options, start=1):
            print(f"{number}. {option}")
    
    choice = choose_integer(1, len(options))
    chosen_index = choice - 1
    return options[chosen_index]

def choose_integer(min: int, max: int) -> int:
    while True:
        user_input = input(f"Make a choice by typing an integer in the range {min} to {max}: ").strip()
        try:
            choice = int(user_input)
            if choice >= min and choice <= max:
                return choice
        except:
            print("The input is not an integer, try again.")
        else:
            print("Invalid choice, try again.")