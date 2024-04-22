import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

city_name = input("Enter required city name: ")

API_KEY = os.getenv("API_KEY")

query_string = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

response = requests.get(query_string).json()

pprint.pprint(response)

print("Weather Information:")
print(f"{response['name']} - {response['main']['temp']}°C")

