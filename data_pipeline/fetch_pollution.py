import os
import requests
import pandas as pd

CITY = "Bengaluru"
URL = "https://api.openaq.org/v3/latest"
CSV_PATH = os.path.join(os.path.dirname(__file__), '../data/pollution_data.csv')
os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)

params = {"city": CITY, "limit": 100}
response = requests.get(URL, params=params)
print("API Status Code:", response.status_code)

if response.status_code != 200:
    raise Exception(f"Failed to fetch data: {response.status_code}")

data = response.json()
records = []

for result in data.get('results', []):
    for measurement in result.get('measurements', []):
        records.append({
            "city": CITY,
            "location": result.get('location'),
            "parameter": measurement.get('parameter'),
            "value": measurement.get('value'),
            "unit": measurement.get('unit'),
            "timestamp": measurement.get('lastUpdated')
        })

if not records:
    raise Exception("No data fetched. CSV not created.")

df_pollution = pd.DataFrame(records)
df_pollution.to_csv(CSV_PATH, index=False)
print(f"Pollution data saved at {CSV_PATH}")
print(df_pollution.head())
