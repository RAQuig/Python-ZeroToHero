"""
LESSON 2: Dictionaries
Dictionaries store data in key-value pairs. They allow fast lookups by key name.
"""

# Creating a dictionary
player_stats = {
    "username": "ShadowCoder",
    "level": 12,
    "class": "Rogue",
    "gold": 350
}

# Accessing values
print(f"Player: {player_stats['username']}")
print(f"Class: {player_stats.get('class')}")

# Safely accessing a key that might not exist using .get(key, default)
mana = player_stats.get("mana", 0)  # Returns 0 if "mana" key doesn't exist
print(f"Mana: {mana}")

# Modifying and adding key-value pairs
player_stats["gold"] += 50         # Update existing key
player_stats["is_online"] = True   # Add new key
print("Updated Stats:", player_stats)

# Nested Dictionaries & Lists
guild = {
    "guild_name": "Infinite Loop",
    "members": [
        {"name": "Alex", "role": "Leader"},
        {"name": "Sam", "role": "Officer"}
    ]
}

# Accessing nested data
leader_name = guild["members"][0]["name"]
print(f"Guild Leader: {leader_name}")

# ✏️ PRACTICE EXERCISE:
# Create a dictionary representing a shop inventory where keys are item names
# and values are prices. Loop through it using .items() and print each item with its price.
