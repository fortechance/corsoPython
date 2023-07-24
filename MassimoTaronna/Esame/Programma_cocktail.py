import PySimpleGUI as sg
import csv

# Funzione per leggere i dati da un file CSV
def leggi_dati_da_csv(file_path):
    dati = []

    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Salta l'intestazione

        for row in csv_reader:
            dati.append(row)

    return dati

# Carica i dati dei cocktail e degli ingredienti dai file CSV
cocktails = leggi_dati_da_csv("cocktails.csv")
ingredienti = leggi_dati_da_csv("ingredienti.csv")

# Layout dell'interfaccia grafica
layout = [
    [sg.Text("Seleziona un cocktail:")],
    [sg.Listbox([cocktail[0] for cocktail in cocktails], size=(40, 12), key="-COCKTAILS-", select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],
    [sg.Button("Crea Cocktail"), sg.Button("Esci")],
    [sg.Text(size=(30, 50), justification='right', key="-OUTPUT-")]
]

# Crea la finestra dell'applicazione
window = sg.Window("Cocktail App", layout, size=(800,680), background_color="lightgreen")

# Ciclo di eventi per l'interazione con l'interfaccia grafica
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Esci"):
        break
    
    if event == "Crea Cocktail":
        cocktail_scelto = values["-COCKTAILS-"][0]

        # Trova il cocktail selezionato nella lista dei cocktail
        for cocktail in cocktails:
            if cocktail[0] == cocktail_scelto:
                ingredienti_cocktail = cocktail[1].split(', ')
                quantita_cocktail = list(map(int, cocktail[2:]))

                # Controlla la disponibilità degli ingredienti per il cocktail selezionato
                ingredienti_sufficienti = True
                for ingrediente, quantita in zip(ingredienti_cocktail, quantita_cocktail):
                    for ingrediente_magazzino in ingredienti:
                        if ingrediente_magazzino[0] == ingrediente:
                            quantita_magazzino = int(ingrediente_magazzino[1])
                            if quantita_magazzino < quantita:
                                ingredienti_sufficienti = False
                                break
                    if not ingredienti_sufficienti:
                        break

                # Se gli ingredienti sono sufficienti, sottrai le quantità utilizzate
                if ingredienti_sufficienti:
                    for ingrediente, quantita in zip(ingredienti_cocktail, quantita_cocktail):
                        for ingrediente_magazzino in ingredienti:
                            if ingrediente_magazzino[0] == ingrediente:
                                ingrediente_magazzino[1] = str(int(ingrediente_magazzino[1]) - quantita)

                    # Aggiorna l'output nella finestra
                    output_text = f"Hai creato il cocktail '{cocktail_scelto}'\nIngredienti utilizzati:\n"
                    for ingrediente, quantita in zip(ingredienti_cocktail, quantita_cocktail):
                        output_text += f"{ingrediente}: {quantita}\n"
                    output_text += "\nQuantità aggiornate degli ingredienti:\n"
                    for ingrediente in ingredienti:
                        output_text += f"{ingrediente[0]}: {ingrediente[1]}\n"
                    window["-OUTPUT-"].update(output_text)
                    break
                else:
                    sg.popup_error("Ingredienti insufficienti per creare il cocktail!")
                    break

# Aggiorna i dati nei file CSV con le quantità aggiornate degli ingredienti
with open("ingredienti.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Ingrediente", "Quantità"])
    for ingrediente in ingredienti:
        csv_writer.writerow(ingrediente)

        

# Chiudi la finestra quando il ciclo di eventi termina
window.close()
