nomeFile = "pierobianco/CSVOrigine.csv"
sep = ";"
priKey = 0

with open(nomeFile,"r") as f: #apro il file in modalità lettura (r = read, w=write. a=append)
    buffer = f.read() #apro il file
    righe = buffer.split("\n") #split delle righe del csv alla fine della riga
    print(righe)
    print(len(righe)) #stampa quante righe mi ha tirato fuori
    riga1 = len(righe[0])
    dictDati = {}
    
    for riga in righe:
        if riga != "":#controllo che la mia riga abbia almeno 1 carattere | len(riga) > 1
            colonne = riga.split(sep) #divido la riga per separatore
            if len(colonne) != riga1:#il csv è formato da 4 colonne, se ce n'è di più non è valido
                print("separatore errato")
            else:
                if (colonne[0]=="Cognome" and colonne[1]=="Nome"):
                    pass #non fare nulla, salta
                else:
                    priKey += 1
                    print(f"id = {priKey} -> {colonne}")
        else:#se la riga è minore di 1 vuol dire che è vuota | riga vuota
            print("Nessun valore in questa riga")