import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
API_KEY = os.getenv("OPENAQ_API_KEY")

# Define the city and API endpoint
CITY = "Bengaluru"
URL = "https://api.openaq.org/v3/latest"

# Set up the headers with the API key
headers = {
    "X-API-Key": API_KEY
}

# Define the parameters for the API request
params = {
    "city": CITY,
    "limit": 100
}

# Make the API request
response = requests.get(URL, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
