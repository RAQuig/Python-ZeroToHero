"""
MODULE 3 PROJECT: OOP Weather Dashboard & Bot
Instructions: This script uses an Object-Oriented design pattern to fetch
and display weather forecasts using live web APIs.
"""

import requests
import sys

class WeatherClient:
    """Client class responsible for communicating with the external Weather API."""
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, lat, lon, city_name):
        self.lat = lat
        self.lon = lon
        self.city_name = city_name

    def fetch_weather(self):
        """Fetches current weather parameters."""
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            "current_weather": True
        }
        try:
            res = requests.get(self.BASE_URL, params=params, timeout=5)
            res.raise_for_status()
            return res.json().get("current_weather", {})
        except requests.exceptions.RequestException as e:
            print(f"❌ API Error for {self.city_name}: {e}")
            return None


class WeatherReport:
    """Class responsible for formatting and presenting weather data."""
    def __init__(self, city_name, weather_data):
        self.city_name = city_name
        self.temp = weather_data.get("temperature", "N/A")
        self.windspeed = weather_data.get("windspeed", "N/A")
        self.is_day = weather_data.get("is_day", 1) == 1

    def display(self):
        day_icon = "☀️ Day" if self.is_day else "🌙 Night"
        print("\n" + "=" * 35)
        print(f" 📍 WEATHER REPORT: {self.city_name.upper()}")
        print("=" * 35)
        print(f" Time of Day: {day_icon}")
        print(f" Temperature: {self.temp}°C")
        print(f" Wind Speed:  {self.windspeed} km/h")
        print("=" * 35)


class DashboardApp:
    """Main Application Manager handling location targets and user loop."""
    # Pre-configured popular cities with coordinates
    PRESETS = {
        "1": ("Saskatoon", 52.1332, -106.6700),
        "2": ("Toronto", 43.6532, -79.3832),
        "3": ("Vancouver", 49.2827, -123.1207),
        "4": ("London", 51.5074, -0.1278),
        "5": ("Tokyo", 35.6762, 139.6503)
    }

    def run(self):
        while True:
            print("\n--- 🌍 OOP WEATHER DASHBOARD ---")
            for key, (city, _, _) in self.PRESETS.items():
                print(f"{key}. {city}")
            print("6. Exit")

            choice = input("\nSelect a city (1-6): ").strip()

            if choice == "6":
                print("Closing Dashboard. Goodbye!")
                break

            if choice in self.PRESETS:
                city, lat, lon = self.PRESETS[choice]
                client = WeatherClient(lat, lon, city)
                raw_data = client.fetch_weather()

                if raw_data:
                    report = WeatherReport(city, raw_data)
                    report.display()
            else:
                print("❌ Invalid selection. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    app = DashboardApp()
    app.run()
