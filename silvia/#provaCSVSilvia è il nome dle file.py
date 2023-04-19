#provaCSVSilvia è il nome dle file
import json

NomeFile = "silvia/CSVOriginesilvia.CSV"
Separatore = ";"

with open(NomeFile,'r' ) as f:
    #f.writer("ciao")
    buffer = f.read()

print(buffer)

righe = buffer.split('\n')
print(righe)
print(len(righe))

priKey = 0
dictDati = {}
dictCampi = {}

for riga in righe:
    colonne = riga.split(Separatore)
    print(colonne)

for riga in righe:
    
    if(len(riga) > 1):
        dictCampi = {}
        colonne = riga.split(Separatore)
        if len(colonne)  !=4:
            print("Separatore errato")
        else:
            if (colonne [0] == 'Cognome' and colonne [1] == 'Nome'):
                #titoli delle colonne li salto
                
                pass
            else: 
                 priKey += 1
                 print(f'chiave: {priKey} -> contenuto: {colonne}')

            dictCampi['Cognome'] = colonne [0]
            dictCampi['Nome'] = colonne [1]
            dictCampi['Professione'] = colonne [2]
            dictCampi['eta'] = colonne[3]          
            dictDati[priKey] = dictCampi.copy()
           
        dictDati[priKey] = dictCampi

        print(colonne)
   

        Dascrivere = json.dumps(dictDati)
        print(Dascrivere)
        with open(NomeFile + 'json', 'w') as f:
          f.write(Dascrivere)

    else:
        #print('trovata riga vuota')
        pass


