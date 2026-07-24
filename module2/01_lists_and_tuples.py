"""
LESSON 1: Lists & Tuples
Lists are mutable (changeable) sequences. Tuples are immutable (cannot change once created).
"""

# 1. Lists (Mutable)
inventory = ["Potion", "Shield", "Mana Elixir"]
inventory.append("Iron Sword")  # Add item
inventory.remove("Shield")      # Remove item
print("Updated Inventory:", inventory)

# Indexing & Slicing
first_item = inventory[0]
first_two = inventory[:2]
print(f"First item: {first_item} | First two: {first_two}")

# 2. Tuples (Immutable - great for coordinates, RGB colors, or fixed settings)
screen_resolution = (1920, 1080)
# screen_resolution[0] = 1280  # ❌ This will raise an Error! Tuples can't be modified.

width, height = screen_resolution  # Unpacking a tuple
print(f"Width: {width}px, Height: {height}px")

# 3. List Comprehensions (Clean, single-line loops for building lists)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Standard way:
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# List comprehension way (Cleaner!):
squared_evens = [n**2 for n in numbers if n % 2 == 0]
print("Squared Even Numbers:", squared_evens)

# ✏️ PRACTICE EXERCISE FOR YOU AND YOUR FRIENDS:
# Given a list of prices = [12.99, 5.50, 25.00, 3.00], use a list comprehension
# to create a new list called 'discounted' with 10% off each price!
