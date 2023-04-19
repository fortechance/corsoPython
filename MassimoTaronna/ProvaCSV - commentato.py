# Decidere il nome del file.

import json

NomeFile = 'Desktop/corsoPython/MassimoTaronna/CSVOrigine.csv'      # percorso e nome file da aprire
Separatore = ';'                                                    # definizione del separatore campi del file CSV

with open(NomeFile,'r') as f:                                       # apro il file in lettura 'r'
    buffer = f.read()                                               # carico il file in 'buffer'

print(buffer)                                                       # visualizzo a schermo il contenuto di 'buffer'

righe = buffer.split('\n')                                          # divido le righe in corrsipondenza del comando a capo '\n'
print(righe)                                                        # visualizzo a schermo le singole righe
print(len(righe))                                                   # conto il numero di righe

priKey = 0                                                          # definisco una chiave primaria che parte da 0
dictDati = {}                                                       # definisco un dizionario dati
dictCampi = {}                                                      # definisco un dizionario campi

DaScrivere =""

for riga in righe:                                                  # per ogni riga
    
    if (len(riga) > 1):                                             # se la lunghezza è maggiore di 1
        dictCampi = {}                                              # azzero ad ogni riga il dizionario campi
        colonne = riga.split(Separatore)                            # creo le colonne dividendo le righe in corrispondenza del separatore
        if len(colonne) != 4:                                       # se il numero di colonne è diverso da 4
            print("Separatore errato")                              # visualizzo 'separatore errato'
        else:                                                       # oppure
            if (colonne[0]=='Cognome' and colonne[1] =='Nome'):     # se le colonne contengono il nome dei campi, li salto
                pass 
            else:                                                   # oppure
                priKey += 1                                         # aumento la chiave primaria di 1 per ogni linea
                print(f'chiave: {priKey} -> contenuto: {colonne}')  # visualizzo i dati con la chiave primaria

                dictCampi['Cognome'] = colonne[0]                   # riempio il dizionario 
                dictCampi['Nome'] = colonne[1]
                dictCampi['Professione'] = colonne[2]
                dictCampi['eta'] = colonne[3]
                dictDati[priKey] = dictCampi.copy()

            DaScrivere = json.dumps(dictDati)
            print(DaScrivere)
            with open(NomeFile + '.json','w') as f:
                f.write(DaScrivere)        


    else:
        #print('trovata riga vuota')
        print(['None', 'None', 'None', 'None'])

print(DaScrivere)