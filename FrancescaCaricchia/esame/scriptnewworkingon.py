import csv
import PySimpleGUI as sg

def leggi_csv(file_path):
    dati = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for riga in reader:
            dati.append(riga)
    return dati

dati_ricette = leggi_csv("C:\\Users\\Utente\\CorsoPython\\CorsoPython\\FrancescaCaricchia\\esame\\lista_ricette.csv")
dati_prodotti = leggi_csv("C:\\Users\\Utente\\CorsoPython\\CorsoPython\\FrancescaCaricchia\\esame\\lista_prodotti.csv")

def crea_menu(dati_ricette):
    menu = []
    for row in dati_ricette:
        menu.append(f"{row[0]}. {row[1]}")
    print("Menu creato:", menu)
    return menu

def ottieni_ricetta(drink_id, dati_ricette):
    for row in dati_ricette:
        if int(row[0]) == drink_id:
            return row[2].split(',')
    return []

def ottieni_ingredienti_iniziali(dati_prodotti):
    ingredienti_iniziali = []
    for row in dati_prodotti:
        nome_ingrediente = row[1]
        quantita_iniziale = int(row[2])
        ingredienti_iniziali.append((nome_ingrediente, quantita_iniziale))
    #print("Ingredienti ottenuti:", ingredienti)
    return ingredienti_iniziali

def ottieni_ingredienti_aggiornati(dati_prodotti_copia):
    ingredienti_aggiornati = []
    for row in dati_prodotti_copia:
        nome_ingrediente = row[1]
        quantita_aggiornata = int(row[2])
        ingredienti_aggiornati.append((nome_ingrediente, quantita_aggiornata))
    #print("Ingredienti ottenuti:", ingredienti)
    return ingredienti_aggiornati

def eroga_drink(drink_id, dati_ricette, dati_prodotti):
    ingredienti_mancanti = 0
    for row in dati_ricette:
        if int(row[0]) == drink_id:
            ricetta = row[2].split(',')
            for ingrediente in ricetta:
                ingrediente = ingrediente.strip()
                for prodotto in dati_prodotti:
                    if ingrediente.lower() == prodotto[1].lower():
                        quantita = int(prodotto[2])
                        if quantita >= 50:
                            prodotto[2] = str(quantita - 50)
                        else:
                            ingredienti_mancanti += 1
                        break
                else:
                    continue
                break
    return ingredienti_mancanti

def aggiorna_quantita_ingredienti(file_path, dati_prodotti):
    with open(file_path, 'w', newline ='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Ingrediente', 'Quantita'])
        for prodotto in dati_prodotti:
            writer.writerow(prodotto)

def crea_finestra_ingredienti_iniziali(ingredienti_iniziali):
    layout = [
        [sg.Text("Lista degli ingredienti iniziali:")],
        [sg.Listbox(values=ingredienti_iniziali, size=(50, 6), key='-LISTA-INGREDIENTI-INIZIALI-')],
    ]
    window = sg.Window("Ingredienti iniziali", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()

def crea_finestra_ingredienti_aggiornati(ingredienti_aggiornati):
    layout = [
        [sg.Text("Quantità disponibili dopo l'erogazione:")],
        [sg.Listbox(values=ingredienti_aggiornati[:], size=(50, 6), key='-LISTA-INGREDIENTI-AGGIORNATI-')],
    ]
    window = sg.Window("Ingredienti aggiornati", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()

def main():
    dati_ricette_copia = list(dati_ricette)
    dati_prodotti_copia = list(dati_prodotti)

    ingredienti_iniziali = ottieni_ingredienti_iniziali(dati_prodotti_copia)
    ingredienti_aggiornati = ottieni_ingredienti_aggiornati(dati_prodotti_copia)
    
    layout = [
        [sg.Text("Benvenuto nel Distributore del Sorriso!")],
        [sg.Text("Come posso aiutarti?")],
        [
            sg.Column([
                [sg.Text("Menu:")],
                [sg.Listbox(values=crea_menu(dati_ricette_copia), size=(50,6), key='-MENU-')],
            ]),
            sg.Column([
                [sg.Text("Lista degli ingredienti:")],
                [sg.Listbox(values=ottieni_ingredienti_iniziali(dati_prodotti), size=(50,6), key='-INGREDIENTI-INIZIALI-')],
            ]),
            sg.Column([
                [sg.Text("Quantita disponibili:")],
                [sg.Listbox(values=ingredienti_aggiornati, size=(50,6), key='-INGREDIENTI-AGGIORNATI-')],
            ])
        ],
        [
            sg.Slider(range=(1, 10), default_value = 1, orientation = 'h', size=(20,15), key='-QUANTITA-'),
            sg.Button("Eroga"), 
            sg.Button("Esci")
        ]
    ]

    window = sg.Window("Distributore del sorriso", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Esci":
            break

        menu_selection = values['-MENU-']
        if menu_selection and len(menu_selection) > 0: 
            scelta = int(menu_selection[0].split('.')[0])
            quantita = int(values['-QUANTITA-'])
            ingredienti_mancanti = eroga_drink(scelta, dati_ricette, dati_prodotti)

            if ingredienti_mancanti == 0:
                for _ in range(quantita):
                    ricetta = ottieni_ricetta(scelta, dati_ricette)
                    sg.popup("Erogazione in corso: " + ", ".join(ricetta))
                
                # Aggiornamento della finestra degli ingredienti iniziali
                window_ingredienti_iniziali = sg.Window("Ingredienti iniziali", layout=[
                    [sg.Text("Lista degli ingredienti iniziali:")],
                    [sg.Listbox(values=ottieni_ingredienti_iniziali(dati_prodotti), size=(50, 6))],
                ])
                window_ingredienti_iniziali.close()

                
                # Aggiornamento della finestra degli ingredienti aggiornati
                ingredienti_aggiornati = ottieni_ingredienti_aggiornati(dati_prodotti)
                window_ingredienti_aggiornati = sg.Window("Ingredienti aggiornati", layout=[
                    [sg.Text("Quantità disponibili dopo l'erogazione:")],
                    [sg.Listbox(values=ingredienti_aggiornati, size=(50, 6))],
                ])
                window_ingredienti_aggiornati.close()

                # Aggiornamento del file CSV con le quantità aggiornate
                aggiorna_quantita_ingredienti("lista_prodotti.csv", dati_prodotti)
                window['-INGREDIENTI-AGGIORNATI-'].update(values=ingredienti_aggiornati)
            else:
                sg.popup(f"Mi dispiace, ingredienti esauriti. Impossibile erogare il drink.")

    window.close()

if __name__ == "__main__":
    main()