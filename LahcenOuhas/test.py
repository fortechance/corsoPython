import csv
with open('filename.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')