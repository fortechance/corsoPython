import csv
with open('file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    first = True
    for riga in csv_reader:
        if first:
            #saltiamo la prima riga, quella di intestazione
            first = False
            continue
        print(riga["Nome"], riga["Cognome"], "ha", riga["Età"], "anni")
        #Mario Rossi ha 20 anni