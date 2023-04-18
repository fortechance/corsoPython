#esercizio Fede Casa 18 aprile

NomeFile = 'FedericaPuddinu/CSVOrigineFede.csv'
Separatore = ';'

with open(NomeFile,'r') as f:

    buffer=f.read()

print(buffer)

righe = buffer.split('\n')
print(righe)
print(len(righe))

priKey = 0
dictDati = {}
dictCampi = {}

for riga in righe:
    
    if(len(riga) > 1):
        colonne = riga.split(Separatore)

