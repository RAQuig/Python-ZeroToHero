"""
LESSON 4: Functions
Functions package code into reusable chunks so you can call them anytime.
"""

# 1. Defining a basic function with parameters and a return statement
def calculate_damage(base_attack, multiplier):
    """Calculates total attack damage."""
    total_damage = base_attack * multiplier
    return total_damage

# Calling the function
hit_1 = calculate_damage(15, 1.5)
hit_2 = calculate_damage(20, 2.0)

print(f"Hit 1 dealt {hit_1} damage.")
print(f"Hit 2 dealt {hit_2} damage.")

# 2. Function with default parameters
def spawn_enemy(enemy_type="Goblin", hp=50):
    print(f"A wild {enemy_type} appears with {hp} HP!")

spawn_enemy()                   # Uses defaults ("Goblin", 50)
spawn_enemy("Dragon", 500)      # Overrides defaults

# ✏️ PRACTICE EXERCISE:
# Create a function named 'heal_player' that takes 'current_hp' and 'heal_amount',
# adds them together, caps max HP at 100, and returns the new HP.
