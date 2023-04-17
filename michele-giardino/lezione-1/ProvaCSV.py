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

print(buffer)
# stampa il contenuto del file

righe = buffer.split("\n")
#split dele righe del csv

prikey = 0 #chiave di partenza

for riga in righe:
    if len(riga) > 1: #contrllo che la mia riga abbia almeno un carattere
        colonne = riga.split(Separatore) #divido la riga per separatore
        if len(colonne) != 4: #il csv è formato da 4 colonne, se ce n'è una in più non è valido
            print("separatore errato")
        else:
            if (colonne[0]=='Cognome'and colonne[1] =='Nome'):
                #salto i titoli delle colonne: Cognome e Nome
                pass
            else:
                prikey += 1 #aumenta il valore della chiave +1 ad ogni nuovo contenuto
                print(f'chiave: {prikey} -> contenuto: {colonne}') #stampa la chiave ad ogni contenuto
    else:#se la riga è minore di 1 vuol dire che è vuota
        print("Nessun valore in questa riga") #ad esempio un a capo vuoto

print(len(righe))
#stampa quante righe mi hai letto

#ditCampi e ditDati fare in modo che davanti ad ogni dato ci sia il nome del campo di riferimento