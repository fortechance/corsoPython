#definisco la classe casa
class casa:
    def __init__(self, piano, denom, mq):
        self.piano = piano
        self.denom = denom
        self.mq = int(mq)

#la classe attico eredita da casa
class attico(casa):
    def __init__(self, piano, denom, mq, mqterrazzo):
        #eredito il costruttore della classe casa
        super().__init__(piano, denom, mq)
        self.mqterrazzo = mqterrazzo
        
class condominio():
    def __init__(self, nome):
        self.elencoCase = {} #lista al cui interno metto le case componenti il condominio
        self.totMq = 0
        self.nomeCondominio = nome #nome del condominio preso da file .csv
        
    #mi aspetto che c abbia un valore di tipo casa (valore più generico)
    def aggiungiCasa(self, c:casa):
        casaMq = c.mq #i mq della casa ereditano da c (casa) .mq passati tramite la definizione della classe casa
        denom = c.denom
        
        try: #prova ad aggiungere la casa e ad aggiornare i MQ
            self.elencoCase[denom] = c
            self.totMq += casaMq
        except:# se non aggiunge non faccio nulla
            pass
            
    def calcoloMillesimi(self, denominazione):
        mq = self.elencoCase[denominazione].mq # al dizionario elencoscase assegno alla chiave denom il valore mq
        millesimi = 1000*mq/self.totMq #calcolo dei millesimi
        
        return millesimi 
    
class quartiere():
    def __init__(self, csvCondominio):
        self.condomini = {}
        with open(csvCondominio) as f: #apro il file e lo chiudo quando non viene utilizzato
            buffer = f.read()
            
            appartamenti = buffer.split("\n") #divido per le linee del csv
            
            for app in appartamenti:
                dati = app.split(";") #divido la linea per :; presenti
                #dati sarà un array (lista) di campi
                
                idCond = dati[0] #dati[0] = idCondominio da csv (sarà la chiave del dizionario condomini)
                piano = dati[1] #dati[1] = Piano (Valori da passare alla classe casa)
                denom = dati[2] #dati[2] = Denom
                mq = dati[3] #dati[3] = MQ
                print(mq)
                
                if (idCond in self.condomini.keys()):#se il condominio non esiste, lo creo
                    pass
                else:
                    #se il condominio non esiste, lo creo
                    self.condomini[idCond] = condominio(idCond)
                    #aggiungo la casa con il metodo aggiungicasa
                self.condomini[idCond].aggiungiCasa(casa(piano, denom, mq))
                
        