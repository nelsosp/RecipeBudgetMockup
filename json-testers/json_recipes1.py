import json
import pandas as pd


with open('responserecipes1.json', 'r') as f:
    data = json.load(f)

# for item in data['recipes']:
#     print(item['title'], item['ingredients'])

df = pd.json_normalize(data['recipes'])

print(df.head())
