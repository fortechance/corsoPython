import json

nomeFile = "pierobianco/CSVOrigine.csv"
sep = ";"
priKey = 0

with open(nomeFile,"r") as f: #apro il file in modalità lettura (r = read, w=write. a=append)
    buffer = f.read() #apro il file
righe = buffer.split("\n") #split delle righe del csv alla fine della riga \n

#print(righe[0]) #stampa Nome;Cognome;
Riga1 = righe[0].count(";") + 1 #conto quanti valori ci sono nella prima riga separati da ;
#print (Riga1)

#print(len(righe)) #stampa quante righe mi ha tirato fuori
dictDati = {} #inizializzo il dizionario
dictCampi = {}
DaScrivere = ""

for riga in righe: #per ogni riga dell'array righe
    if riga != "":#controllo che la mia riga abbia almeno 1 carattere | len(riga) > 1
        dictCampi = {} #azzero il dizionario campi
        colonne = riga.split(sep) #divido la riga per separatore Nome, Cognome...
        #print(f"colonne:{colonne[0]}, {colonne[1]}") #stampa Nome, Cognome....
        
        if len(colonne) != Riga1:#se le colonne sono diverse dal conteggio dei valori della prima riga
            print("separatore errato")
        else:
            if (colonne[0]=="Cognome" and colonne[1]=="Nome"):
                pass #non fare nulla, salta
            else:
                dictDati[priKey]={}
                dictCampi["Nome"] = colonne[0]
                dictCampi["Cognome"] = colonne[1]
                dictCampi["Professione"] = colonne[2]
                dictCampi["Eta"] = colonne[3]
                dictDati[priKey].update(dictCampi) #dictDati = {1:{"Nome":"Rossi", Cognome:Mario,...}}
                #print(f'chiave: {priKey} -> contenuto: {colonne}')
                priKey += 1 #incremento di 1 la primary key (id univoco)
                
                DaScrivere = json.dumps(dictDati)
                print(DaScrivere)
                #with open(NomeFile + '.json','w') as f: #Creo il file json
                    #f.write(DaScrivere) #Scrivo il file json
    else:#se la riga è minore di 1 vuol dire che è vuota | riga vuota
        print(['None', 'None', 'None', 'None'])