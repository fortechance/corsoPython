# Decidere il nome del file.
import json
NomeFile = 'LahcenOuhas/csv.csv'
Separatore = ';'
with open(NomeFile,'r') as pippo:
    #f.write("ciao")

    buffer = pippo.read()

print(buffer)

righe = buffer.split('\n')
print(righe)
print(len(righe))


priKey = 0
dictDati = {}
dictCampi = {}

DaScrivere = ""


for riga in righe:
    
    if (len(riga) > 1):
        colonne = riga.split(Separatore)
        if len(colonne) != 4:
            print("Separatore errato")
        else:
            if (colonne[0]=='Cognome' and colonne[1] =='Nome'):
                #titoli delle colonne, li salto
                pass 
            else:
             #priKey += 1
             print(f'chiave: {priKey} -> contenuto: {colonne}')
            dictCampi[priKey] =  {'Cognome': colonne[0], 'Nome':colonne[1],'Professione' :colonne[2],'eta' : colonne[3]}
            #dictCampi['Cognome'] = colonne[0]
             # dictCampi['Nome'] = colonne[1]
            # dictCampi['Professione'] = colonne[2]
              #dictCampi['eta'] = colonne[3]
            #dictDati[priKey].update(dictCampi)   
            DaScrivere = json.dumps(dictDati)
            print(DaScrivere)
   

            priKey += 1

        dictDati[priKey] = dictCampi
        

    else:
        #print('trovata riga vuota')
        
        print(['None', 'None', 'None', 'None'])
with open(NomeFile + '.json','w') as f:
          f.write(DaScrivere)
print(DaScrivere)