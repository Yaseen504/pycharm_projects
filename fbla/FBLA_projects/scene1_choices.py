from utilities import (
    clear_terminal
)
from scene1_events import (
    explore_cave, go_swimming
)

def handle_choices(player):

    """Handles the player's choices in Scene 1."""

    while True:
        print("While you're outdoors, you want explore somewhere before you "
              "return home")
        print("1 - Explore a cave")
        print("2 - Go out swimming")
        print("stop - Leave story\n")

        choice = input('Choice: ').strip()
        clear_terminal()

        if choice == "1":
            explore_cave(player)
            return "scene1_choice1"
        elif choice == '2':
            go_swimming(player)
            return "scene1_choice1"
        elif choice.lower() == "stop":
            print("Exiting the story.")
            break
        else:
            print("Invalid choice. Try again.")
