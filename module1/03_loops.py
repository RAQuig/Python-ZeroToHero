"""
LESSON 3: Loops (for, while)
Loops repeat blocks of code so you don't have to write repetitive instructions.
"""

print("--- 1. FOR LOOP (Iterating over a list) ---")
inventory = ["Health Potion", "Iron Sword", "Shield", "Magic Scroll"]

# 'item' takes the value of each list element one by one
for item in inventory:
    print(f"Inventory Item: {item}")

print("\n--- 2. FOR LOOP (Counting with range) ---")
# Counts from 1 up to (but not including) 6
for round_num in range(1, 6):
    print(f"Starting Round {round_num}!")

print("\n--- 3. WHILE LOOP (Runs until condition becomes False) ---")
boss_hp = 30

while boss_hp > 0:
    print(f"Boss HP: {boss_hp}. You attack for 10 damage!")
    boss_hp -= 10  # Decrements boss_hp by 10 each loop iteration

print("Victory! The boss has been defeated.")

# ✏️ PRACTICE EXERCISE:
# Write a for loop that prints every even number from 2 to 20.
