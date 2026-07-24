"""
LESSON 3: File Handling (Text & JSON)
Reading and writing files allows you to save application state permanently.
"""

import json

# 1. Writing to a plain text file using 'with' (automatically handles closing the file)
with open("notes.txt", "w") as file:
    file.write("Python Module 2\n")
    file.write("File handling made easy!\n")

# Reading from a text file
with open("notes.txt", "r") as file:
    content = file.read()
    print("--- Text File Content ---")
    print(content)

# 2. Working with JSON (JavaScript Object Notation) - standard format for web & app data
data_to_save = {
    "game_title": "Dungeon Escape",
    "high_score": 1420,
    "achievements_unlocked": ["First Win", "Treasure Hunter"]
}

# Saving Python dict -> JSON file
with open("save_data.json", "w") as json_file:
    json.dump(data_to_save, json_file, indent=4)
print("Data successfully saved to save_data.json!")

# Reading JSON file -> Python dict
with open("save_data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("\n--- Loaded JSON Data ---")
print(f"High Score: {loaded_data['high_score']}")
print(f"Achievements: {', '.join(loaded_data['achievements_unlocked'])}")

# ✏️ PRACTICE EXERCISE:
# Add a new achievement to loaded_data["achievements_unlocked"] and resave it back to save_data.json!
