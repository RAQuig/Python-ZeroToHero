"""
LESSON 3: Working with APIs (HTTP GET Requests)
APIs allow your code to fetch real-world data across the web.
Make sure you run 'pip install requests' first!
"""

import requests

# Public API endpoint (returns a random university or space data)
API_URL = "https://api.open-meteo.com/v1/forecast"

# Parameters passed as a dictionary (latitude/longitude for Saskatoon)
params = {
    "latitude": 52.1332,
    "longitude": -106.6700,
    "current_weather": True
}

print("Fetching data from weather API...")

try:
    # Send HTTP GET request
    response = requests.get(API_URL, params=params, timeout=5)
    
    # Check if request succeeded (HTTP Status Code 200)
    response.raise_for_status()
    
    # Parse raw response into a Python dictionary
    data = response.json()
    
    current = data.get("current_weather", {})
    temp = current.get("temperature")
    wind = current.get("windspeed")
    
    print("\n--- Live Data Received ---")
    print(f"Current Temperature: {temp}°C")
    print(f"Wind Speed: {wind} km/h")

except requests.exceptions.RequestException as error:
    print(f"❌ Failed to reach API: {error}")

# ✏️ PRACTICE EXERCISE:
# Look up the latitude/longitude of another city and change the 'params' dictionary
# to display that location's weather!
