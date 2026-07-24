"""
LESSON 1: Variables & Data Types
Variables hold data in memory. Python determines the type automatically.
"""

# 1. String (Text)
player_name = "Alex"

# 2. Integer (Whole numbers)
player_level = 1

# 3. Float (Decimal numbers)
health_points = 98.5

# 4. Boolean (True or False)
is_alive = True

# Printing variables using f-strings (formatted text)
print(f"Player: {player_name}")
print(f"Level: {player_level}")
print(f"Health: {health_points}")
print(f"Active Status: {is_alive}")

# Type checking (Run this to see what data types Python assigned)
print("\n--- Data Types ---")
print(type(player_name))  # <class 'str'>
print(type(player_level)) # <class 'int'>
print(type(health_points))# <class 'float'>
print(type(is_alive))     # <class 'bool'>

# ✏️ PRACTICE EXERCISE FOR YOU AND YOUR FRIENDS:
# Create 3 variables describing a item in a game (item_name, cost, is_equipped)
# and print them using an f-string below!
