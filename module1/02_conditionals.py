"""
LESSON 2: Conditionals (if, elif, else)
Conditionals allow your program to make decisions based on logical conditions.
"""

player_score = 85

# Basic decision chain
if player_score >= 90:
    print("Rank: S Class")
elif player_score >= 70:
    print("Rank: A Class")
elif player_score >= 50:
    print("Rank: B Class")
else:
    print("Rank: Needs Practice!")

# Logical operators: and, or, not
has_key = True
door_unlocked = False

if has_key and not door_unlocked:
    print("\nYou use your key to unlock the door.")
    door_unlocked = True

# Getting user input dynamically
print("\n--- Interactive Check ---")
user_age = int(input("Enter your age: "))

if user_age >= 13:
    print("Access granted! Welcome to the game.")
else:
    print("Sorry, you must be at least 13 years old.")

# ✏️ PRACTICE EXERCISE:
# Write a script that asks for a player's gold, and prints if they can afford
# a health potion that costs 50 gold.
