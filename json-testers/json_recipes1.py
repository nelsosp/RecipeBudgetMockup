import json
import pandas as pd


# with open('responserecipes1.json', 'r') as f:
#     data = json.load(f)

# for item in data['recipes']:
#     print(item['title'], item['ingredients'])

# df = pd.json_normalize(data['recipes'])

# print(df.head())

with open('responserecipes1.json', 'r') as f:
    data = json.load(f)

for item in data.get('recipes', []):
    title = item.get('title', 'Title not available')
    ingredients = item.get('ingredients', [])

    print("Title:", title)
    print("Ingredients:")

    for ingredient_info in ingredients:
        ingredient = ingredient_info.get('ingredient')
        print("- ", ingredient)

    print("\n")
