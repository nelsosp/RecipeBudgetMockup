import json


with open('response.json', 'r') as f:
    data = json.load(f)

for item in data['results']['search_results']:
    print(item['ProductName'], item['Price'])

