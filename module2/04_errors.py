"""
LESSON 4: Error Handling (try / except / else / finally)
Catch errors gracefully so your program doesn't crash unexpectedly.
"""

# 1. Basic try/except block
try:
    number = int(input("Enter a divisor number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")

except ZeroDivisionError:
    print("❌ Error: You cannot divide by zero!")

except ValueError:
    print("❌ Error: That was not a valid whole number!")

# 2. Handling File Errors
filename = "missing_config.json"

try:
    with open(filename, "r") as f:
        data = f.read()
except FileNotFoundError:
    print(f"⚠️ Warning: '{filename}' was not found. Creating default configuration...")
    # Safe fallback action:
    data = '{"setting": "default"}'

# 3. Complete structure with else and finally
try:
    file = open("notes.txt", "r")
except FileNotFoundError:
    print("File missing.")
else:
    # Runs ONLY if no exceptions were raised in 'try'
    print("\nFile opened successfully.")
    print(f"Line count: {len(file.readlines())}")
finally:
    # ALWAYS runs no matter what (great for clean-up tasks)
    print("Execution complete.")

# ✏️ PRACTICE EXERCISE:
# Write a function 'convert_to_float(val)' that attempts to cast 'val' to float.
# Return None if it raises a ValueError.
