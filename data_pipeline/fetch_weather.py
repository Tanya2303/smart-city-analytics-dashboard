import os
import requests
from dotenv import load_dotenv

# Since data_pipeline is sibling of backend, go up one folder, then into backend/
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'backend')
env_path = os.path.join(BASE_DIR, '.env')

load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Check your .env file!")

CITY = "Bengaluru"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

response = requests.get(URL)
data = response.json()

print(data)
