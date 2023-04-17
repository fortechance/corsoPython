# Decidere il nome del file e il separatore tra un elemento e l'altro.

NomeFile = 'michele-giardino/CSVOrigine.csv'
Separatore = ';'

f = open(NomeFile,'r')

   buffer = f.read()

print(buffer)