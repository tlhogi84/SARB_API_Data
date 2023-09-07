import requests
import pandas as pd
import xml.etree.ElementTree as ET
import os
import datetime

setwd = os.chdir(r'C:\Users\Tlhogi\Documents\Grace\Investment Work\4. Sovereign Bonds\South Africa\Market_Rates')

api_url = "https://custom.resbank.co.za/SarbWebApi/MCM/Contributions/VALRATES"

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

df       = pd.DataFrame(data)
xml_data = df["XMLData"].values[0]

root = ET.fromstring(xml_data)

data = []

for line in root.findall(".//Line"):
    columns = line.findall("./Column")
    column_values = [col.text if col.text else "None" for col in columns]
    data.append(column_values)
    
df = pd.DataFrame(data, columns=["Column", "Text"])
df = df[~df['Text'].isin(['None', '0.00'])]
df.reset_index(drop=True, inplace=True)


current_date = datetime.date.today()

if current_date.weekday() in {0, 5, 6}:  # Monday, Saturday, or Sunday
    previous_working_day = current_date - datetime.timedelta(days=3)
else:
    previous_working_day = current_date - datetime.timedelta(days=1)

date_str = previous_working_day.strftime('%Y%m%d')

csv_file_name = f'{date_str}_Rates.csv'

# Save the DataFrame to the CSV file
df.to_csv(csv_file_name)
