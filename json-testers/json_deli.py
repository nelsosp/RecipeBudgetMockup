import json
import pandas as pd


with open('responsedeli1.json', 'r') as f:
    data = json.load(f)

for item in data['results']['search_results']:
    print(item['ProductName'], item['Price'])

df = pd.json_normalize(data['results']['search_results'])

# # print(df.head())
