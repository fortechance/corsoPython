NomeFile = 'CSVcausale.csv'
Separatore = ';'

with open(NomeFile,'r') as f:
    buffer = f.read()

print(buffer)

righe = buffer.split('\n')
print(righe)
print(len(righe))

priKey = 1
dictDati = {}
dictCampi = {}

DaScrivere = ""

for riga in righe:
    
    if (len(riga) > 1):
        #dictCampi = {}
        colonne = riga.split(Separatore)
        if len(colonne) != 3:
            print("Separatore errato")
        else:
            if (colonne[0]=='Cognome' and colonne[1] =='Nome'):
                #titoli delle colonne, li salto
                pass 
            else:
                dictDati[priKey]={}
                print(f'chiave: {priKey} -> contenuto: {colonne}')
                #dictCampi['Key'] = priKey
                dictCampi['Codice'] = colonne[0]
                dictCampi['Descrizione'] = colonne[1]
                dictCampi['Segno'] = colonne[2]
                dictDati[priKey].update(dictCampi)

                priKey += 1

    else:
        pass

print(DaScrivere)

