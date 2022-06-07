import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv('API_KEY')

# Get geolocation
api_url = 'https://ipapi.co/json/'
response = requests.get(api_url)
data = response.json()
lat=data['latitude']
lon=data['longitude']

# Get location
api_url = f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={API_KEY}'
response = requests.get(api_url)
data = response.json()
city = data[0]['name']

# Get weather
# city="Stockholm"
# api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},se&units=metric&lang=se&appid={API_KEY}'
api_url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=se&appid={API_KEY}'
response = requests.get(api_url)
data = response.json()
temp = data['main']['temp']
desc = data['weather'][0]['description']

# print(json.dumps(data, indent=2))
print(f'Weather in {city}: {desc} {round(temp)} C')