import sqlite3
import tkinter as tk
from tkinter import messagebox

def get_recipes(ingredients):
    con = sqlite3.connect('drinks.db')
    cur = con.cursor()
    cur.execute("SELECT name FROM recipes WHERE ingredients LIKE ?", ('%' + ingredients + '%',))
    recipes = cur.fetchall()
    con.close()
    return [recipe[0] for recipe in recipes]

def search_recipes():
    ingredients = entry_ingredients.get()
    matching_recipes = get_recipes(ingredients)

    if matching_recipes:
        result_text.set("\n".join(matching_recipes))
    else:
        result_text.set("No matching recipes found.")

# Create the main application window
app = tk.Tk()
app.title("Drink Recipe Finder")

# Create and set up GUI components
frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

label_instructions = tk.Label(frame, text="Enter the ingredients you have (comma-separated):")
label_instructions.pack()

entry_ingredients = tk.Entry(frame, width=50)
entry_ingredients.pack(pady=10)

button_search = tk.Button(frame, text="Search Recipes", command=search_recipes)
button_search.pack(pady=10)

result_text = tk.StringVar()
label_result = tk.Label(frame, textvariable=result_text, justify="left")
label_result.pack()

app.mainloop()