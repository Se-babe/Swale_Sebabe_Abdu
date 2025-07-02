#create an account from https://openweathermap.org/users/sing_up
# Define the API endpoint
#url = f"https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API_KEY}"

#define the api endpoints

import requests
import pandas as pd

API_KEY = "aeee9d9a475d066f100fbcaf8da302c6"  
lat = 35.6895
lon = 139.6917

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data['list'])  # Flattens nested data
    df.to_csv('weather_data.csv', index=False)
    print("Weather data saved to 'weather_data.csv'")
else:
    print(f"Error: {response.status_code} - {response.text}")
