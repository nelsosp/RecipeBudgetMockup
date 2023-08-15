import pandas as pd
import ast  # Library for safely parsing the JSON-like structure

# Load data from CSV file
csv_filename = 'recipe1.csv'  # Replace with your CSV file name
loaded_df = pd.read_csv(csv_filename)

# Create a list to store formatted data
formatted_data = []

# Iterate through each row
for index, row in loaded_df.iterrows():
    title = row['title']

    # Safely parse the 'ingredients' column as a list of dictionaries
    ingredients_list = ast.literal_eval(row['ingredients'])

    # Create a new row for each ingredient
    for ingredient in ingredients_list:
        formatted_data.append(
            {'Title': title, 'Ingredient': ingredient['ingredient']})

# Create a DataFrame from the formatted data
formatted_df = pd.DataFrame(formatted_data)

# Export DataFrame to Excel
excel_filename = 'formatted_recipes_eachcell.xlsx'
formatted_df.to_excel(excel_filename, index=False)
