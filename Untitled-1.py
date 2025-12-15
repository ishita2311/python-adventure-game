# -------------------------------------------------------
# adventure_game.py
# -------------------------------------------------------
# This script implements a text-based adventure game
# where the player explores different paths and makes
# decisions to find a hidden treasure.
# -------------------------------------------------------

def start_game():
    """
    This function starts the adventure game.
    It introduces the story, takes the player's name,
    and asks for the first choice.
    """
    print("\nWelcome to the Legendary Treasure Adventure!")
    
    # Ask player name
    name = input("Enter your name, brave explorer: ")
    print(f"\nHello {name}! Your quest is to find the hidden treasure.")

    # Initial choice
    while True:
        print("\nChoose your path:")
        print("1. Enter the dark forest")
        print("2. Explore the mysterious cave")

        choice = input("Enter 1 or 2: ")

        if choice == "1":
            forest_path()
            break
        elif choice == "2":
            cave_path()
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


def forest_path():
    """
    This function handles the forest scenario.
    The player makes a decision that determines the outcome.
    """
    print("\nYou step into the dark forest.")
    print("The forest is quiet and you hear water flowing nearby.")

    print("\nWhat do you do?")
    print("1. Follow the river")
    print("2. Climb a tall tree to look around")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou follow the river and discover a hidden treasure chest!")
        end_game("win")
    elif choice == "2":
        print("\nYou fall from the tree and get injured.")
        end_game("lose")
    else:
        print("Invalid choice.")
        forest_path()


def cave_path():
    """
    This function handles the cave scenario.
    The player must choose wisely to survive.
    """
    print("\nYou enter the mysterious cave.")
    print("It is dark and you hear strange noises.")

    print("\nWhat do you do?")
    print("1. Light a torch")
    print("2. Walk forward in the dark")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nThe torch reveals a treasure hidden behind rocks!")
        end_game("win")
    elif choice == "2":
        print("\nYou fall into a pit and the adventure ends.")
        end_game("lose")
    else:
        print("Invalid choice.")
        cave_path()


def end_game(result):
    """
    This function ends the game based on the result
    and provides an option to restart.
    """
    if result == "win":
        print("\nCongratulations! You found the legendary treasure!")
    else:
        print("\nGame Over! Better luck next time.")

    restart = input("\nDo you want to play again? (yes/no): ").lower()

    if restart == "yes":
        start_game()
    else:
        print("\nThank you for playing the adventure game!")


# -------------------------------
# Start the game
# -------------------------------
start_game()
