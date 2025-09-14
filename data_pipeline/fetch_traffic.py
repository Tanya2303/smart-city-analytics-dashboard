import pandas as pd
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'backend', 'db')
csv_path = os.path.join(BASE_DIR, 'Banglore_traffic_Dataset.csv')

df = pd.read_csv(csv_path)
print(df.head())
