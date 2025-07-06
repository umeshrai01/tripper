import os
from dotenv import load_dotenv
load_dotenv()

from src.llm import initiate_llm
from src.tools.attract_activities import exploration
from src.tools.lodging import hotels
from src.tools.weather_analysis import get_real_time_weather

print("--- Testing Gemini API ---")
try:
    llm = initiate_llm()
    response = llm.invoke("Hello, how are you?")
    print(f"Gemini API Test Success: {response.content[:50]}...")
except Exception as e:
    print(f"Gemini API Test Failed: {e}")

print("\n--- Testing Tavily API (Attractions) ---")
try:
    exp = exploration()
    attraction_results = exp.search_attraction("London")
    print(f"Tavily API (Attractions) Test Success: {attraction_results.content[:50]}...")
except Exception as e:
    print(f"Tavily API (Attractions) Test Failed: {e}")

print("\n--- Testing Tavily API (Lodging) ---")
try:
    hotel_finder = hotels()
    lodging_results = hotel_finder.find_hotels("Paris")
    print(f"Tavily API (Lodging) Test Success: {lodging_results.content[:50]}...")
except Exception as e:
    print(f"Tavily API (Lodging) Test Failed: {e}")

print("\n--- Testing OpenWeatherMap API ---")
try:
    weather_data = get_real_time_weather("New York")
    print(f"OpenWeatherMap API Test Success: {weather_data[:50]}...")
except Exception as e:
    print(f"OpenWeatherMap API Test Failed: {e}")
