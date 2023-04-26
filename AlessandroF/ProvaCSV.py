# coding=utf-8
# Decidere il nome del file.
import json   #importo libreria json
print 
NomeFile = 'CSVOrigine.csv' #su mac guarda la directory del file
Separatore = ';'

with open(NomeFile,'r') as f:  #apro il file in letture (r)
    #f.write("ciaoddddddd") #te
    buffer = f.read()   #metto nella variabile buffer i dati

print(buffer)          # printo buffer

righe = buffer.split('\n')  #splitto buffer per gli a capo e metto dentro righe
print('sto printando righe:')    #printo righe
print(righe)    #printo righe
print('sto printando lunghezza di righe:')    #printo righe
print(len(righe))  #printo lalunghezza di righe

priKey = 0
dictDati = {}
dictCampi = {}  #Dizionario campi

for riga in righe:
    
    if (len(riga) > 1):
        dictCampi = {}  # azzero il dizionario campi per ogni ciclo
        colonne = riga.split(Separatore) #se il numero di caratteri nella riga è maggiore di uno allora  
        if len(colonne) != 4:     #controllo se il numero di colonne è diverso da 4
            print("Separatore errato")   #avviso che è errato 
        else:                                                    #altrimenti (allora le colonne sono 4)
            if (colonne[0]=='Cognome' and colonne[1] =='Nome'):  #se  i valori delleprime due celle sono Cognome e Nome non faccio nulla perchè sono nell'intestazione
                #titoli delle colonne, li salto
                pass 
            else:                                                 #altrimenti siamo nella prima riga utile e 
                priKey += 1                                          #aggiungo uno alla chiave primaria
                print('printo lachiave ed il contenuti delle colonne:')
                print(f'chiave: {priKey} -> contenuto: {colonne}')   #printo la chiave primaria ed il contenuto della variabile colonne

                dictCampi['Cognome'] = colonne[0]       #riempio il dizionario campi
                dictCampi['Nome'] = colonne[1]
                dictCampi['Professione'] = colonne[2]
                dictCampi['eta'] = colonne[3]

                dictDati[priKey] = dictCampi.copy()  # ?????nel dizionatio campi avra nella chiave uno come contenuto quello didizionarioCampi. Uso il copy altrimenti 
            
            DaScrivere = json.dumps(dictDati) #ildizionario dati una volta elaborato lo metti nella variabile DaScrivere in json
            print(DaScrivere)
            with open(NomeFile + '.json', 'w') as f:  #scrivo un nuovo file con lo stesso nome di quello di partenzapiù esensione json
                f.write(DaScrivere)
        dictDati[priKey] = dictCampi    

      

    else:
        #print('trovata riga vuota')
        print(['None', 'None', 'None', 'None'])
print('printo il dizionario \'dicDATI:\'')
print(dictDati)