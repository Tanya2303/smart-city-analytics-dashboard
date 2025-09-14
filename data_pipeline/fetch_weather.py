import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load API key
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'backend', '.env'))
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Bengaluru"

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

weather_dict = {
    "city": CITY,
    "temperature": data['main']['temp'],
    "humidity": data['main']['humidity'],
    "weather": data['weather'][0]['description'],
    "timestamp": datetime.now()
}

df_weather = pd.DataFrame([weather_dict])

# Save to CSV (append if file exists)
csv_path = os.path.join(os.path.dirname(__file__), '../data/weather_data.csv')
if os.path.exists(csv_path):
    df_weather.to_csv(csv_path, mode='a', header=False, index=False)
else:
    df_weather.to_csv(csv_path, index=False)

print("Weather data saved:")
print(df_weather)
