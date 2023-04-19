nomeFile = "pierobianco/CSVOrigine.csv"
sep = ";"
priKey = 0

with open(nomeFile,"r") as f: #apro il file in modalità lettura (r = read, w=write. a=append)
    buffer = f.read() #apro il file
    righe = buffer.split("\n") #split delle righe del csv alla fine della riga \n
    #print(righe[0]) #stampa Nome;Cognome;
    #print(len(righe)) #stampa quante righe mi ha tirato fuori
    dictDati = {} #inizializzo il dizionario
    dictCampi = {}
    
    for riga in righe: #per ogni riga dell'array
        if riga != "":#controllo che la mia riga abbia almeno 1 carattere | len(riga) > 1
            dictCampi = {}
            colonne = riga.split(sep) #divido la riga per separatore
            #print(f"colonne:{colonne[0]}, {colonne[1]}") #stampa Nome, Cognome....
            print (len(colonne))
            if len(colonne) != 4:#se le prime due colonne sono Nome, Cognome
                print("separatore errato")
            else:
                if (colonne[0]=="Cognome" and colonne[1]=="Nome"):
                    pass #non fare nulla, salta
                else:
                    priKey += 1 #incremento di 1 la primary key (id univoco)
                    print(f"id = {priKey} -> {colonne}")
                    dictCampi["Nome"] = colonne[0]
                    dictCampi["Cognome"] = colonne[1]
                    dictCampi["Professione"] = colonne[2]
                    dictCampi["Eta"] = colonne[3]
                    dictDati["priKey"] = priKey #dictDati = {1:{"Nome":"Rossi", Cognome:Mario,...}}
        else:#se la riga è minore di 1 vuol dire che è vuota | riga vuota
            print("Nessun valore in questa riga")