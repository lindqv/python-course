from dungeon import Room
from characters import Player
from items import Dice

def choose_action(room: Room, player: Player, dice: Dice):
    actions = ["Attack", "Skip turn"]
    choice = choose(actions, "What would you like to do?")

    if choice == "Attack":
        enemy_to_attack = choose(room.enemies, "Which enemy would you like to attack?")
        ability = choose(player.abilities, "Which ability would you like to use?")
        player.attack(enemy_to_attack, ability, dice)

        if enemy_to_attack.is_defeated():
            room.enemies.remove(enemy_to_attack)
            print(enemy_to_attack.name, "was defeated!")
            experience = enemy_to_attack.calculate_experience_points()
            player.gain_experience_points(experience)
    else:
        return

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
    user_input = input(f"Make a choice by typing an integer in the range {min} to {max}: ").strip()
    try:
        choice = int(user_input)
        if choice < min or choice > max:
            print("Choice out of range, try again.")
            choose_integer(min, max)
        else:
            return choice
    except:
        print("Invalid choice, try again.")
        choose_integer(min, max)