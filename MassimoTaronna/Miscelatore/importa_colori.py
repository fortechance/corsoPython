import csv
import os

import os

def main():
    # Definisci il percorso della directory dei file da eseguire
    directory_path = "C:/Users/massi/Desktop/corsoPython/MassimoTaronna/Miscelatore"


def import_csv(file_path):
    fields = []
    records = []

    with open("./prodotti.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        fields = next(reader)  # Legge la prima riga come intestazione dei campi

        for row in reader:
            records.append(row)

    return fields, records

def main():
    file_path = "prodotti.csv"
    fields, records = import_csv(file_path)

    print("Campi:")
    print(fields)

    print("\nRecord:")
    for record in records:
        print(record)

if __name__ == "__main__":
    main()
