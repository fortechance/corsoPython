import PySimpleGUI as sg

cocktails = {
    "Mojito": ["Rum", "Mint leaves", "Lime juice", "Sugar", "Soda water"],
    "Martini": ["Gin", "Dry vermouth", "Green olive"],
    "Cosmopolitan": ["Vodka", "Triple sec", "Lime juice", "Cranberry juice"],
    # Aggiungi gli altri cocktail qui...
}

ingredient_stock = {
    "Rum": 10,
    "Mint leaves": 20,
    "Lime juice": 15,
    "Sugar": 30,
    "Soda water": 25,
    "Gin": 12,
    "Dry vermouth": 8,
    "Green olive": 40,
    "Vodka": 18,
    "Triple sec": 10,
    "Cranberry juice": 0,  # Esempio: Cranberry juice è esaurito
    # Aggiungi gli altri ingredienti qui...
}

def create_layout():
    cocktail_list = list(cocktails.keys())

    preparable_cocktails = []
    unpreparable_cocktails = []

    for cocktail, ingredients in cocktails.items():
        if all(ingredient_stock.get(ingredient, 0) > 0 for ingredient in ingredients):
            preparable_cocktails.append(cocktail)
        else:
            unpreparable_cocktails.append(cocktail)

    layout = [
        [sg.Text("La fabbrica del sorriso", font=("Helvetica", 20), justification="center")],
        [sg.Text("Un contributo alla spensieratezza", font=("Helvetica", 12), justification="center")],
        [sg.Text("Seleziona un cocktail:")],
        [sg.Listbox(preparable_cocktails, size=(30, 6), key="-PREPARABLE_COCKTAILS-")],
        [sg.Text("Cocktail non preparabili:")],
        [sg.Listbox(unpreparable_cocktails, size=(30, 6), key="-UNPREPARABLE_COCKTAILS-")],
        [sg.Button("Prepara cocktail"), sg.Button("Esci")],
        [sg.Text("Scorte degli ingredienti:")],
        [sg.Table(values=[[ingredient, quantity] for ingredient, quantity in ingredient_stock.items()],
                  headings=["Ingrediente", "Quantità"],
                  auto_size_columns=True,
                  display_row_numbers=False,
                  num_rows=min(25, len(ingredient_stock)), key="Table")],
        [sg.Text("Aggiungi quantità di un ingrediente:")],
        [sg.InputText(key="-INGREDIENT-"), sg.InputText(key="-QUANTITY-", size=(5, 1)), sg.Button("Aggiungi")]
    ]
    return layout


def main():
    window = sg.Window("Cocktail Maker", create_layout(), resizable=True, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Esci":
            break

        if event == "Prepara cocktail":
            selected_cocktail = values["-PREPARABLE_COCKTAILS-"][0]

            if selected_cocktail:
                ingredients_needed = cocktails[selected_cocktail]
                missing_ingredients = []

                for ingredient in ingredients_needed:
                    if ingredient_stock.get(ingredient, 0) <= 0:
                        missing_ingredients.append(ingredient)

                if missing_ingredients:
                    missing_ingredients_str = ", ".join(missing_ingredients)
                    sg.popup_error(f"Impossibile preparare il cocktail. Mancano gli ingredienti: {missing_ingredients_str}")
                else:
                    print(f"Preparazione del cocktail: {selected_cocktail}")
                    for ingredient in ingredients_needed:
                        ingredient_stock[ingredient] -= 1
                        print(f"Utilizzato 1 unità di {ingredient}")
                    print("Cocktail pronto!")

                # Aggiorna la tabella delle scorte nella GUI
                window["Table"].update(values=[[ingredient, quantity] for ingredient, quantity in ingredient_stock.items()])

        if event == "Aggiungi":
            ingredient = values["-INGREDIENT-"]
            try:
                quantity = int(values["-QUANTITY-"])
            except ValueError:
                sg.popup_error("Inserire una quantità valida.")
                continue

            if ingredient in ingredient_stock:
                ingredient_stock[ingredient] += quantity
            else:
                ingredient_stock[ingredient] = quantity

            # Aggiorna la tabella delle scorte nella GUI
            window["Table"].update(values=[[ingredient, quantity] for ingredient, quantity in ingredient_stock.items()])

            # Resetta i valori degli input
            window["-INGREDIENT-"].update("")
            window["-QUANTITY-"].update("")

            # Aggiorna l'elenco dei cocktail non preparabili
            preparable_cocktails = []
            unpreparable_cocktails = []

            for cocktail, ingredients in cocktails.items():
                if all(ingredient_stock.get(ingredient, 0) > 0 for ingredient in ingredients):
                    preparable_cocktails.append(cocktail)
                else:
                    unpreparable_cocktails.append(cocktail)

            window["-PREPARABLE_COCKTAILS-"].update(values=preparable_cocktails)
            window["-UNPREPARABLE_COCKTAILS-"].update(values=unpreparable_cocktails)

    window.close()


if __name__ == "__main__":
    main()
