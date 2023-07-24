import csv
with open("./dati.csv", newline="") as filecsv:
    lettore = csv.reader(filecsv, delimiter=",")
    header = next(lettore)
    print (header)