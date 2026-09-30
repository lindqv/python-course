from game import Game
from user_input import choose

class StartScreen:
    def __init__(self, title: str, options: list[str]):
        self.title = title
        self.options = options

    def display(self):
        print(self.title)

    def choose_mode(self):
        return choose(self.options, "Choose an option to start the game:")

start_screen = StartScreen("Green Dragon Quest: a dungeon crawler adventure", ["Start game", "Automatic mode (for testing)"])
start_screen.display()
choice = start_screen.choose_mode()
print(choice)

if choice == "Start game":
    Game().play()
else:
    Game(interactive=False).play()