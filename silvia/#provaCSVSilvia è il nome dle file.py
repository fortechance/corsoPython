#provaCSVSilvia è il nome dle file

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
dictcampi = {}

for riga in righe:
    colonne = riga.split(Separatore)

    print(colonne)

for riga in righe:
    if(len(riga) > 1):
        colonne = riga.split(Separatore)
        if len(colonne)  !=4:
            print("Separatore errato")
        else:
            if (colonne [0] == 'Cognome' and colonne [1] == 'Nome'):
                #titoli delle colonne li salto
                for colonna in colonne:
                    dictcampi[nomecolonna] = {}
                pass
            else: 
                priKey: += 1
            print(f'chiave: {priKey} -> contenuto: {colonne}')

            dictcampi['Cognome'] = colonna [0]
            dictcampi['Nome'] = colonna [1]
            dictcampi['Professione'] = colonna [2]
                      

            dictDati[priKey] = dictcampi

            print(colonne)
    else:
        #print('trovata riga vuota')

