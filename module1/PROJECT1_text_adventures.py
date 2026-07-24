"""
MODULE 1 PROJECT: Text Adventure Game
Instructions: Run this script to play the base game, then modify it with 
your friends to add new rooms, combat options, or inventory systems!
"""

def start_game():
    print("=" * 40)
    print("      WELCOME TO THE DUNGEON ESCAPE     ")
    print("=" * 40)
    
    player_name = input("Enter your hero's name: ")
    print(f"\nWelcome, {player_name}! You wake up in a dark, cold stone cell.")
    
    # Start room choice
    first_choice(player_name)

def first_choice(player_name):
    print("\nYou see two doors ahead of you:")
    print("1. A heavy wooden door on the left.")
    print("2. A rusted iron grate on the right.")
    
    choice = input("\nWhich path do you choose? (1 or 2): ")
    
    if choice == "1":
        wooden_door_room(player_name)
    elif choice == "2":
        iron_grate_room(player_name)
    else:
        print("Invalid choice! A mysterious trap door opens beneath you...")
        print("GAME OVER")

def wooden_door_room(player_name):
    print(f"\n{player_name} enters a brightly lit room filled with treasure chests!")
    print("You find a bag of gold and a key to the castle gates.")
    print("🎉 YOU WIN AND ESCAPE RICH!")

def iron_grate_room(player_name):
    print(f"\n{player_name} steps into a damp cave... You hear heavy breathing.")
    print("A sleeping guard wakes up and spots you!")
    
    action = input("Do you FIGHT or RUN? ").lower()
    
    if action == "run":
        print("You run as fast as you can back to the start!")
        first_choice(player_name)
    else:
        print("You try to fight empty-handed, but the guard overwhelms you.")
        print("💀 GAME OVER")

# Entry point of the script
if __name__ == "__main__":
    start_game()
