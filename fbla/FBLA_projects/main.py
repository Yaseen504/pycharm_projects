# Standard library imports

# Imports from FBLAclasses module


from game_state import game_state
from instructions import game_instructions
from prologue import prologue

# General imported modules
from utilities import clear_terminal


# Scene 1 imported modules


# Main Menu Functions
def main_story():
    clear_terminal()

    prologue()
    game_state()


def game_main_menu():
    done = False
    while not done:  # Infinite choice loop if invalid input
        clear_terminal()
        print("Main Menu")
        print("FBLA Project\n")
        print("Title: Dreamland\n")
        print("Menu")
        print("S - Start Game")
        print("I - Instructions")
        print("Q - Quit\n")
        choice = input("Choice: ").upper()
        if choice == "S":
            main_story()
        elif choice == "I":
            game_instructions()
        elif choice == "Q":
            print("Quitting!")
            break
        else:
            clear_terminal()
            print("Invalid, try again!")


if __name__ == "__main__":
    game_main_menu()

# todo fix the display condtionally function
# todo add distinct colors to dialouge and text
