import csv
import tkinter as tk
from tkinter import messagebox
import os

def load_cocktail_data(file_path):
    cocktail_data = []
    
    BASE = 'C:\\Users\\louhas.ALASCOM\\OneDrive\\Documenti\\GitHub\\corsoPython\\LahcenOuhas\\Esame\\'

    file = os.path.join(BASE, file_path )
    with open(file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cocktail_data.append(row)
    return cocktail_data


def search_cocktails():
    ingredients = entry_ingredients.get()
    ingredients = [ingredient.strip().lower() for ingredient in ingredients.split(',')]
    matching_cocktails = [cocktail['name'] for cocktail in cocktail_data if all(ingredient in cocktail['ingredients'].lower() for ingredient in ingredients)]

    if matching_cocktails:
        result_text.set("\n".join(matching_cocktails))
    else:
        messagebox.showinfo("Nessun cocktail corrispondente", "Nessun cocktail corrispondente trovato.")

# Carica i dati dei cocktail da un file CSV
cocktail_data = load_cocktail_data('cocktails.csv')

# Crea la finestra principale dell'applicazione
app = tk.Tk()
app.title("Cocktail App")

# Crea e imposta i componenti della GUI
frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

label_instructions = tk.Label(frame, text="Inserisci gli ingredienti che hai (separati da virgola):")
label_instructions.pack()

entry_ingredients = tk.Entry(frame, width=50)
entry_ingredients.pack(pady=10)

button_search = tk.Button(frame, text="Cerca Cocktail", command=search_cocktails)
button_search.pack(pady=10)

result_text = tk.StringVar()
label_result = tk.Label(frame, textvariable=result_text, justify="left")
label_result.pack()

app.mainloop()