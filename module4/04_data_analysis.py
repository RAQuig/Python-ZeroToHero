"""
LESSON 4: Data Analysis with Pandas
Pandas is the industry-standard framework for analyzing, filtering, and summarizing datasets.
"""

import pandas as pd

# Sample dataset dictionary
data = {
    "Student": ["Alex", "Sam", "Jordan", "Taylor", "Morgan"],
    "Module1_Score": [95, 88, 76, 92, 84],
    "Module2_Score": [90, 85, 80, 95, 78],
    "Tracks": ["Game Dev", "Web Dev", "Data Science", "Game Dev", "Web Dev"]
}

# Load into Pandas DataFrame (2D Tabular Data)
df = pd.DataFrame(data)

print("--- Full Dataset ---")
print(df)

# Computing summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Filtering data
game_devs = df[df["Tracks"] == "Game Dev"]
print("\n--- Game Dev Track Students ---")
print(game_devs[["Student", "Module1_Score"]])

# Calculating a new calculated column
df["Average_Score"] = (df["Module1_Score"] + df["Module2_Score"]) / 2
print("\n--- Final Scores with Averages ---")
print(df[["Student", "Average_Score"]].sort_values(by="Average_Score", ascending=False))

# ✏️ PRACTICE EXERCISE:
# Filter the DataFrame to show only students who scored above 85 in Module1_Score!
