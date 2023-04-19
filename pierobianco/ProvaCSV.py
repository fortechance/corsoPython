# Decidere il nome del file.
import json

NomeFile = 'pierobianco/CSVOrigine.csv'
Separatore = ';'

with open(NomeFile,'r') as f:
    #f.write("ciao")
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
        if len(colonne) != 4:
            print("Separatore errato")
        else:
            if (colonne[0]=='Cognome' and colonne[1] =='Nome'):
                #titoli delle colonne, li salto
                pass 
            else:
                dictDati[priKey]={}
                print(f'chiave: {priKey} -> contenuto: {colonne}')
                #dictCampi['Key'] = priKey
                dictCampi['Cognome'] = colonne[0]
                dictCampi['Nome'] = colonne[1]
                dictCampi['Professione'] = colonne[2]
                dictCampi['Eta'] = colonne[3]
                dictDati[priKey].update(dictCampi)

                priKey += 1

            DaScrivere = json.dumps(dictDati)
            print(DaScrivere)
            with open(NomeFile + '.json','w') as f:
                f.write(DaScrivere)

    else:
        #print('trovata riga vuota')
        print(['None', 'None', 'None', 'None'])

print(DaScrivere)

