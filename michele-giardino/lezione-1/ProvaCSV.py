# Una libreria per visualizzare il tutto sul broswer
import json

# Decidere il nome del file e il separatore tra un elemento e l'altro.

NomeFile = 'CSVOrigine.csv'
Separatore = ';'

# Decido come aprire il file, ovvero cosa devo fare con il file.
# lettura = r
# scrittura = w
# aggiungi = a

f = open(NomeFile,'r')
# Un alternativa potrebbe essere: with open(NomeFile, 'r') as f: = fai questo, finito questo chiudi, chiama questo f.

buffer = f.read()
# .read = leggi

#print(buffer) stampa il contenuto del file, ora lo deselezionato perchè non mi serve

righe = buffer.split("\n")
#split dele righe del csv

prikey = 0 #chiave di partenza
dictCampi = {} #inizializzo il dizionario
dictDati = {}
for riga in righe: #inzia a leggere le righe che voglio vedere
    if (len(riga) > 1): #contrllo che la mia riga abbia almeno un carattere
        dictCampi = {} #ad ogni riga azzera il dizionare campi e ricomincia
        colonne = riga.split(Separatore) #divido la riga per separatore
        if len(colonne) != 4: #il csv è formato da 4 colonne, se ce n'è una in più non è valido
            print("separatore errato")
        else:
            if (colonne[0]=='Cognome'and colonne[1] =='Nome'):
                #salto i titoli delle colonne: Cognome e Nome
                pass
            else:
                dictCampi['Cognome'] = colonne[0]
                dictCampi['Nome'] = colonne[1]
                dictCampi['Professione'] = colonne[2]
                dictCampi['Eta'] = colonne[3]
                
                prikey += 1 #aumenta il valore della chiave +1 ad ogni nuovo contenuto
                print(f'chiave: {prikey} -> contenuto: {dictCampi}') #stampa la chiave ad ogni contenuto
                dictDati[prikey] = dictCampi.copy() #ogni volta che fai il giro in dictDati c'è tutto l'elenco

        print() #stampa un a capo vuoto

    else:#se la riga è minore di 1 vuol dire che è vuota
        print("Nessun valore in questa riga") #ad esempio un a capo vuoto
        print() #stampa un a capo vuoto

print(f'in questo file ci sono: {len(righe)} righe') #stampa quante righe mi hai letto


elaborato = dictDati
with open(NomeFile + 'CC.json','w') as f:
   daScrivere = json.dumps(elaborato)
   f.write(daScrivere)