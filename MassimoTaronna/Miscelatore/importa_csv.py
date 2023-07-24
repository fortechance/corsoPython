import csv

def import_csv("./dati.csv"):
    fields = []
    records = []

    with open("./dati.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        fields = next(reader)  # Legge la prima riga come intestazione dei campi

        for row in reader:
        records.append(row)

    return fields, records

def main():
    file_path = "dati.csv"
    fields, records = import_csv(file_path)

    print("Campi:")
    print(fields)

    print("\nRecord:")
    for record in records:
        print(record)

if __name__ == "__main__":
    main()
