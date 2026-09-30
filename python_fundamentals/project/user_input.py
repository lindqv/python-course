from characters import Player, Character
from items import Dice
from dungeon import Room

def choose_action_in_combat(enemies: list[Character], player: Player, dice: Dice):
    actions = ["Attack", "Skip turn"]
    choice = choose(actions, "What would you like to do?")

    if choice == "Attack":
        enemy_to_attack = choose(enemies, "Which enemy would you like to attack?")
        ability = choose(player.abilities, "Which ability would you like to use?")
        player.attack(enemy_to_attack, ability, dice)
    else:
        return

def choose_action_after_combat(player: Player, room: Room):
    choice = ""
    while choice != "Go to next room":
        choice = choose(["Loot", "Rest", "Go to next room"], "What would you like to do?")
        if choice == "Loot":
            player.loot(room.items)
        elif choice == "Rest":
            player.rest()

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

def choose_integer(min: int, max: int):
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