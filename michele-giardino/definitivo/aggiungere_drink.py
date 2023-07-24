import csv
import os

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

# Avvia il programma interattivo
#crea_file_csv_interattivo()
