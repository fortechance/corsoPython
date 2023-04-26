# Decidere il nome del file.

NomeFile = 'alessandromasini/pierobianco/CSVOriginemasini.csv'
Separatore = ';'

with open(NomeFile,'r') as f:
    #f.write("ciao")
    buffer = f.read()

print(buffer)



righe = buffer.split('\n')
print(righe)
print(len(righe))



priKey = 0
dictDati = {}
dictCampi = {}

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
                priKey += 1
                print(f'chiave: {priKey} -> contenuto: {colonne}')
'''
                dictCampi['Cognome'] = colonne[0]
                dictCampi['Nome'] = colonne[1]
                dictCampi['Professione'] = colonne[2]
                dictCampi['Eta'] = colonne[3]

        dictDati[priKey] = dictCampi



    else:
        #print('trovata riga vuota')
        print(['None', 'None', 'None', 'None'])

print(dictDati)

'''