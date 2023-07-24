import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def importa_file_csv(nome_file):
    records = []
    with open(nome_file, newline='') as file_csv:
        lettore_csv = csv.reader(file_csv)
        intestazione = next(lettore_csv)  # Ottiene l'intestazione del CSV (se presente)

        for riga in lettore_csv:
            record = dict(zip(intestazione, riga)) if intestazione else riga
            records.append(record)

    return records

# Esempio di utilizzo
if __name__ == "__main__":
    nome_file_csv = "prodotti.csv"
    dati = importa_file_csv(nome_file_csv)
    print(dati)

