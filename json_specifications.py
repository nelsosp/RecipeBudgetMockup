import json

with open('response.json', 'r') as f:
    data = json.load (f)


print('results')

# for item in data['results']:
#     print(item['ProductName'])