import PySimpleGUI as sg
import csv
import os

#SU WINDOWS:
#ingredients_file = "ingredients.csv"
#cocktails_file = "cocktails.csv"


# PERMACOS è stato necessario:
# Ottieni il percorso assoluto della cartella del programma
program_folder = os.path.dirname(os.path.abspath(__file__))

# Percorsi assoluti dei file CSV
ingredients_file = os.path.join(program_folder, "ingredients.csv")
cocktails_file = os.path.join(program_folder, "cocktails.csv")

def load_ingredients():
    ingredient_stock = {}
    if os.path.exists(ingredients_file):
        with open(ingredients_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                ingredient = row["Ingredient"]
                quantity = int(row["Quantity"])
                ingredient_stock[ingredient] = quantity
    return ingredient_stock

def load_cocktails():
    cocktails = {}
    if os.path.exists(cocktails_file):
        with open(cocktails_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cocktail = row["Cocktail"]
                ingredients = row["Ingredients"].split(",")
                cocktails[cocktail] = ingredients
    return cocktails

def save_ingredients(ingredient_stock):
    with open(ingredients_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Ingredient", "Quantity"])
        for ingredient, quantity in ingredient_stock.items():
            writer.writerow([ingredient, quantity])

def create_layout():
    ingredient_stock = load_ingredients()
    cocktails = load_cocktails()

    preparable_cocktails = []
    unpreparable_cocktails = []

    for cocktail, ingredients in cocktails.items():
        if all(ingredient_stock.get(ingredient, 0) > 0 for ingredient in ingredients):
            preparable_cocktails.append(cocktail)
        else:
            unpreparable_cocktails.append(cocktail)

    preparable_col = [
        [sg.Text("Seleziona un cocktail:")],
        [sg.Listbox(preparable_cocktails, size=(30, 6), key="-PREPARABLE_COCKTAILS-")],
        [sg.Button("Prepara cocktail")]
    ]

    unpreparable_col = [
        [sg.Text("Cocktail non preparabili:")],
        [sg.Listbox(unpreparable_cocktails, size=(30, 6), key="-UNPREPARABLE_COCKTAILS-")],
        [sg.Button("Mostra ingredienti mancanti")]
    ]

    layout = [
        [sg.Text("La fabbrica del sorriso", font=("Helvetica", 20), justification="center")],
        [sg.Text("Un contributo alla spensieratezza  ;-) ", font=("Helvetica", 12), justification="center")],
        [sg.Column(preparable_col), sg.Column(unpreparable_col)],
        [sg.Button("Esci")],
        [sg.Text("Scorte degli ingredienti:")],
        [sg.Table(values=[[ingredient, quantity] for ingredient, quantity in ingredient_stock.items()],
                  headings=["Ingrediente", "Quantità"],
                  auto_size_columns=True,
                  display_row_numbers=False,
                  num_rows=min(25, len(ingredient_stock)), key="Table")],
        [sg.Text("Aggiungi un ingrediente allo stock:")],
        [sg.InputCombo(values=list(ingredient_stock.keys()), size=(20, 1), key="-ADD_INGREDIENT-"),
         sg.InputText(key="-ADD_QUANTITY-", size=(5, 1)),
         sg.Button("Aggiungi")]
    ]
    return layout

def update_gui(window, ingredient_stock, cocktails):
    preparable_cocktails = []
    unpreparable_cocktails = []

    for cocktail, ingredients in cocktails.items():
        if all(ingredient_stock.get(ingredient, 0) > 0 for ingredient in ingredients):
            preparable_cocktails.append(cocktail)
        else:
            unpreparable_cocktails.append(cocktail)

    window["-PREPARABLE_COCKTAILS-"].update(values=preparable_cocktails)
    window["-UNPREPARABLE_COCKTAILS-"].update(values=unpreparable_cocktails)
    window["Table"].update(values=[[ingredient, quantity] for ingredient, quantity in ingredient_stock.items()])

def missing_ingredients_popup(missing_ingredients):
    ingredients_str = ", ".join(missing_ingredients)
    sg.popup_error(f"Impossibile preparare il cocktail. Mancano gli ingredienti: {ingredients_str}")

def main():
    window = sg.Window("Cocktail Maker", create_layout(), resizable=True, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Esci":
            break

        if event == "Prepara cocktail":
            selected_cocktail = values["-PREPARABLE_COCKTAILS-"]

            if selected_cocktail:
                selected_cocktail = selected_cocktail[0]
                ingredient_stock = load_ingredients()
                cocktails = load_cocktails()
                ingredients_needed = cocktails[selected_cocktail]
                missing_ingredients = []

                for ingredient in ingredients_needed:
                    if ingredient_stock.get(ingredient, 0) <= 0:
                        missing_ingredients.append(ingredient)

                if missing_ingredients:
                    missing_ingredients_popup(missing_ingredients)
                else:
                    for ingredient in ingredients_needed:
                        ingredient_stock[ingredient] -= 1

                update_gui(window, ingredient_stock, cocktails)
                save_ingredients(ingredient_stock)

        if event == "Aggiungi":
            ingredient = values["-ADD_INGREDIENT-"]
            try:
                quantity = int(values["-ADD_QUANTITY-"])
            except ValueError:
                sg.popup_error("Inserire una quantità valida.")
                continue

            ingredient_stock = load_ingredients()
            if ingredient in ingredient_stock:
                ingredient_stock[ingredient] += quantity
            else:
                ingredient_stock[ingredient] = quantity

            update_gui(window, ingredient_stock, cocktails)
            save_ingredients(ingredient_stock)

            # Resetta i valori degli input
            window["-ADD_INGREDIENT-"].update("")
            window["-ADD_QUANTITY-"].update("")

        if event == "Mostra ingredienti mancanti":
            selected_cocktail = values["-UNPREPARABLE_COCKTAILS-"]

            if selected_cocktail:
                selected_cocktail = selected_cocktail[0]
                ingredient_stock = load_ingredients()
                cocktails = load_cocktails()
                ingredients_needed = cocktails[selected_cocktail]
                missing_ingredients = []

                for ingredient in ingredients_needed:
                    if ingredient_stock.get(ingredient, 0) <= 0:
                        missing_ingredients.append(ingredient)

                if missing_ingredients:
                    missing_ingredients_popup(missing_ingredients)

    window.close()

if __name__ == "__main__":
    main()
