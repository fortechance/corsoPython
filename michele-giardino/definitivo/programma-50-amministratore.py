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

def mostra_lista_inventario():
    lista_cocktail = leggi_file_csv(file_bottiglie)

    # Crea una nuova finestra pop-up per mostrare la lista dei cocktail
    popup_window = tk.Toplevel(root)
    popup_window.title("Lista Inventario")

    # Creazione di un Treeview per mostrare i dati
    tree = ttk.Treeview(popup_window)
    tree["columns"] = ("componente", "quantita_ml")
    tree.column("#0", width=0, stretch=tk.NO)  # Nasconde la colonna iniziale
    tree.column("componente", anchor=tk.W, width=200)
    tree.column("quantita_ml", anchor=tk.W, width=100)
    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("componente", text="Componente", anchor=tk.W)
    tree.heading("quantita_ml", text="Quantità (ml)", anchor=tk.W)

    # Inserimento dei dati nel Treeview
    for idx, (componente, quantita_ml) in enumerate(lista_cocktail[1:], start=1):  # Ignora l'intestazione
        tree.insert(parent="", index="end", iid=idx, values=(componente, quantita_ml))

    tree.pack(fill=tk.BOTH, expand=True)



 # Crea una nuova finestra pop-up per mostrare la lista dei cocktail

cocktails = {
    "1": "Mojito",
    "2": "Martini",
    "3": "Sex on the Beach",
    "4": "Negroni",
    "5": "Old Fashioned",
    "6": "Gin and Tonic",
    "7": "White Russian"
}

def mostra_lista_drink():
    lista_cocktail = "\n".join([f"{key}: {value}" for key, value in cocktails.items()])
    messagebox.showinfo("Lista Cocktail", lista_cocktail)



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

    return bottiglie_copia, None

def crea_file_csv_interattivo():
    nome_file = input("Inserisci il nome del drink (senza estensione .csv): ")

    # Verifica se il nome del file termina con ".csv"
    if not nome_file.endswith(".csv"):
        nome_file += ".csv"

    # Controlla se il file esiste già
    if os.path.exists(nome_file):
        print(f"Il file {nome_file} esiste già. Vuoi sovrascriverlo? (S/N)")
        scelta = input().strip().lower()
        if scelta != "s":
            print("Operazione annullata. Il file non è stato modificato.")
            return

    componenti = []
    quantita_ml = []

    print("Inserisci le componenti e le relative quantità (in ml) del drink.")
    print("Per terminare l'inserimento, lasciare vuota la componente.")
    while True:
        componente = input("Componente: ")
        if not componente:
            break
        try:
            quantita = float(input("Quantità (ml): "))
        except ValueError:
            print("La quantità deve essere un numero.")
            continue
        componenti.append(componente)
        quantita_ml.append(quantita)

    # Crea una lista di dizionari con i dati
    dati = [{"componente": c, "quantita_ml": q} for c, q in zip(componenti, quantita_ml)]

    # Scrivi i dati nel file CSV
    with open(nome_file, mode='w', newline='') as file_csv:
        campi = ["componente", "quantita_ml"]
        writer = csv.DictWriter(file_csv, fieldnames=campi)

        # Scrivi l'intestazione dei campi
        writer.writeheader()

        # Scrivi i dati delle componenti e delle quantità
        writer.writerows(dati)

    print(f"Il file {nome_file} è stato creato correttamente con i dati inseriti.")


def main():
    global root
    root = tk.Tk()
    root.title("Distributore del Sorriso")
    root.geometry("700x600")

    # Carica l'immagine
    image = tk.PhotoImage(file=image_path)

    # Mostra l'immagine in un Label
    image_label = tk.Label(root, image=image)
    image_label.pack()

    ttk.Label(root, text="Cosa vuoi aggiornare?").pack()

    # Frame per la riga
    row_frame = tk.Frame(root)
    row_frame.pack()

    # Prima colonna
    column1 = tk.Frame(row_frame)
    column1.pack(side=tk.LEFT, padx=10, pady=5)

    # Aggiungi il gestore di eventi per il pulsante "Lista Drink"
    button1 = tk.Button(column1, text="Lista Drink", width=20, command=mostra_lista_drink)
    button1.pack()

    # Seconda colonna
    column2 = tk.Frame(row_frame)
    column2.pack(side=tk.RIGHT, padx=10, pady=5)

    button2 = tk.Button(column2, text="Lista Inventario", width=20, command=mostra_lista_inventario)
    button2.pack()

    # Terza colonna
    column3 = tk.Frame(row_frame)
    column3.pack(side=tk.RIGHT, padx=10, pady=5)

    button3 = tk.Button(column3, text="Aggiungi drink", width=20, command=crea_file_csv_interattivo)
    button3.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

