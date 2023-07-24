import csv
import copy
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import os

# Ottieni il percorso assoluto della cartella corrente
current_dir = os.path.dirname(os.path.abspath(__file__))
img = 'banner.png'
image_path = os.path.join(current_dir, img)

file_bottiglie = "bottiglie.csv"

def leggi_file_csv(nome_file):
    dati = []
    with open(nome_file, newline='') as file_csv:
        lettore = csv.reader(file_csv)
        for riga in lettore:
            dati.append(riga)
    return dati

def carica_bottiglie(file_bottiglie):
    bottiglie = {}
    dati_bottiglie = leggi_file_csv(file_bottiglie)
    for riga in dati_bottiglie[1:]:  # Ignora l'intestazione
        bottiglia, quantita_ml = riga[0], riga[1]
        bottiglie[bottiglia] = float(quantita_ml)  # Utilizza float() invece di int()
    return bottiglie

def carica_cocktail(file_cocktail):
    cocktail = {}
    dati_cocktail = leggi_file_csv(file_cocktail)
    for riga in dati_cocktail[1:]:  # Ignora l'intestazione
        componente, quantita_ml = riga[0], riga[1]
        cocktail[componente] = float(quantita_ml)
    return cocktail

def calcola_componenti(bottiglie, cocktail_scelto, quantita):
    bottiglie_copia = copy.deepcopy(bottiglie)
    ingredienti_mancanti = set()

    print("\nIngredienti disponibili nelle bottiglie:")
    for bottiglia, quantita_ml in bottiglie_copia.items():
        print(f"{bottiglia}: {quantita_ml} ml")

    for componente, quantita_componente in cocktail_scelto.items():
        quantita_componente *= quantita

        if componente in bottiglie_copia and bottiglie_copia[componente] >= quantita_componente:
            bottiglie_copia[componente] -= quantita_componente
        else:
            ingredienti_mancanti.add(componente)

    if ingredienti_mancanti:
        ingredienti_mancanti_str = ", ".join(ingredienti_mancanti)
        print(f"Non ci sono abbastanza {ingredienti_mancanti_str} per preparare il cocktail.")
        return None, ingredienti_mancanti_str

    return bottiglie_copia, None


def main():
    global root
    root = tk.Tk()
    root.title("Distributore del Sorriso")
    root.geometry("512x600")

    # Carica l'immagine
    image = tk.PhotoImage(file=image_path)

    # Mostra l'immagine in un Label
    image_label = tk.Label(root, image=image)
    image_label.pack()

    ttk.Label(root, text="Cocktail disponibili:").pack()

    cocktails = {
        "1": "Mojito",
        "2": "Martini",
        "3": "Sex on the Beach",
        "4": "Negroni",
        "5": "Old Fashioned",
        "6": "Gin and Tonic",
        "7": "White Russian"
    }

    cocktail_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
    for idx, chiave in enumerate(cocktails.values(), 1):
        cocktail_listbox.insert(idx, chiave)
    cocktail_listbox.pack()

    quantita_label = ttk.Label(root, text="Quanti cocktail vuoi preparare?")
    quantita_label.pack()

    quantita_entry = tk.Entry(root, width=50)
    quantita_entry.pack()

    result_label = ttk.Label(root, text="")
    result_label.pack()

    def show_thankyou_message():
        thankyou_window = tk.Toplevel(root)
        thankyou_window.title("Grazie!")
        thankyou_window.geometry("1280x720")
        ttk.Label(thankyou_window, text="Grazie per aver utilizzato il Distributore del Sorriso. Alla prossima!").pack()

    def prepara_cocktail():
        scelta_cocktail = cocktail_listbox.get(cocktail_listbox.curselection())
        global file_bottiglie  # Rendi la variabile file_bottiglie globale

        if scelta_cocktail not in cocktails.values():
            result_label.config(text="Scelta non valida.")
            return

        file_cocktail = [k for k, v in cocktails.items() if v == scelta_cocktail][0]
        quantita = float(quantita_entry.get())

        bottiglie = carica_bottiglie(file_bottiglie)
        cocktail = carica_cocktail(f"{scelta_cocktail.lower().replace(' ', '_')}.csv")

        bottiglie_aggiornate, ingredienti_mancanti_str = calcola_componenti(bottiglie, cocktail, quantita)

        if ingredienti_mancanti_str:
            result_label.config(text=f"Non ci sono abbastanza {ingredienti_mancanti_str} per preparare il cocktail.")
        else:
            result_label.config(text="Il cocktail è stato realizzato con successo!")

            with open(file_bottiglie, 'w', newline='') as file_csv:
                scrittore = csv.writer(file_csv)
                scrittore.writerow(["Bottiglia", "Quantita_ml"])
                for bottiglia, quantita_ml in bottiglie_aggiornate.items():
                    scrittore.writerow([bottiglia, quantita_ml])

            continuare = messagebox.askyesno("Continuare?", "Vuoi preparare un altro cocktail?")
            if continuare:
                result_label.config(text="")
                quantita_entry.delete(0, tk.END)
            else:
                show_thankyou_message()
                root.destroy()

    tk.Button(
        root, 
        text="Prepara Cocktail",
        width=40,
        height=3,
        bg='#ff5714',
        fg='white', 
        command=prepara_cocktail
    ).pack()

    root.mainloop()

if __name__ == "__main__":
    main()

