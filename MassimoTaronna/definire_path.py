import csv
import os

#intanto devo capire quale path devo utilizzare

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

with open("./dati.csv", newline="") as filecsv:
    lettore = csv.reader(filecsv, delimiter=",")
    header = next(lettore)
    print (header)