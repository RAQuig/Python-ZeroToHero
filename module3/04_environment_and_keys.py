"""
LESSON 4: Managing API Keys & Environment Variables
NEVER hardcode secret API keys into your source code! Store them in a .env file.
"""

import os
from dotenv import load_dotenv

# 1. Load variables from a hidden '.env' file into the environment
load_dotenv()

# 2. Safely retrieve secret variables
api_key = os.getenv("API_KEY", "DEFAULT_DEMO_KEY")
db_password = os.getenv("DB_PASSWORD")

print("--- Environment Config loaded ---")
print(f"Using API Key: {api_key[:4]}**** (Hidden for security)")

if not db_password:
    print("⚠️ Warning: DB_PASSWORD was not set in your .env file!")

"""
HOW TO USE THIS IN YOUR REPO:
1. Create a file named '.env' inside this module folder (it is listed in .gitignore so Git won't commit it).
2. Inside '.env', write key-value pairs like:
   API_KEY="my_secret_token_12345"
   DB_PASSWORD="super_secret_pass"
3. Run this script!
"""
