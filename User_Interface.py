import tkinter as tk
import openpyxl


def on_recipe_select(event):
    selected_index = recipe_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        recipe_name = recipe_listbox.get(selected_index)
        recipe_data = recipes_data[recipe_name]
        ingredients = "\n".join(
            [f"{ingredient}: {price}" for ingredient, price in recipe_data])
        # Calculate total price
        total_price = sum([float(price) for _, price in recipe_data if price])
        selected_recipe_label.config(
            text=f"Ingredients:\n{ingredients}\nTotal Price: {total_price:.2f}")  # Display total price


def filter_recipes():
    max_price = float(price_entry.get())
    filtered_recipes = [recipe for recipe, data in recipes_data.items() if sum(
        [float(price) for _, price in data]) <= max_price]
    recipe_listbox.delete(0, tk.END)
    for recipe in filtered_recipes:
        recipe_listbox.insert(tk.END, recipe)


root = tk.Tk()
root.geometry("600x400")  # Set the initial window size

# Read data from Excel
workbook = openpyxl.load_workbook('Book.xlsx')
sheet = workbook.active

# Create a dictionary to store recipes
recipes_data = {}

for row in sheet.iter_rows(min_row=2, values_only=True):
    # Only extract the relevant columns
    recipe_name, ingredient, _, _, _, total_price = row[:6]
    if recipe_name not in recipes_data:
        recipes_data[recipe_name] = []
    if ingredient and total_price:  # Exclude rows without ingredient or total price
        recipes_data[recipe_name].append((ingredient, total_price))

# Recipe Listbox
# Adjust height and width
recipe_listbox = tk.Listbox(root, height=15, width=40)
for recipe in recipes_data:
    recipe_listbox.insert(tk.END, recipe)
recipe_listbox.bind('<<ListboxSelect>>', on_recipe_select)
recipe_listbox.pack()

# Price Filter Entry and Button
filter_frame = tk.Frame(root)
price_label = tk.Label(filter_frame, text="Enter Max Price:")
price_label.pack(side=tk.LEFT)
price_entry = tk.Entry(filter_frame)
price_entry.pack(side=tk.LEFT)
filter_button = tk.Button(filter_frame, text="Filter", command=filter_recipes)
filter_button.pack(side=tk.LEFT)
filter_frame.pack()

# Selected Recipe Details
# Adjust wraplength and height
selected_recipe_label = tk.Label(root, wraplength=500, height=15)
selected_recipe_label.pack()

root.mainloop()
