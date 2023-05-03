# definire la classe CASA

class casa():

    def __init__(self, piano, denominazione, mq):

        self.piano = piano 
        self.denominazione = denominazione
        self.mq = int(mq)

class attico(casa):

    def __init__(self, piano, denominazione, mq, mqterrazzo):

        casa.__init__(piano,denominazione, mq)
        self.mqterrazzo = mqterrazzo

class condominio():

    def __init__(self, nome):

        self.elencoCase = {} #qui dentro ci metto tutte le case componenti il condominio
        self.totmq = 0
        self.nomeCondominio = nome #questo è il nome del condominio preso dal file .csv
    
    def aggiungiCasa(self, c:casa):

        #devo vedere quanti mq aggiungo per completare il tot mq del condominio
        casamq = c.mq
        denom = c.denominazione
    
        try:
            self.elencoCase[denom] = c
            self.totmq += int(casamq)        
        except:
            pass

    def calcolaMillesimi(self, denominazione):

        mq = self.elencoCase[denominazione].mq
        millesimi = 1000*mq/self.totmq

        return millesimi
    
class quartiere():

    def __init__(self, csvCondominio):

        self.condomini = {}
                
        with open(csvCondominio) as f:
            buffer = f.read()

            appartamenti = buffer.split('\n')  

            for app in appartamenti:
                dati = app.split(';')          

                con = dati[0]
                piano = dati[1]
                den = dati[2]
                mq = dati[3]

                #è ora di creare le istanze...
                
                #intanto bisogna verificare se il condominio esisteo no.

                if ( con in self.condomini.keys()):
                    pass
                else:
                    #il condominio non esiste, lo creo.
                    self.condomini[con] = condominio(con) 

                #adesso aggiungo la casa
                #c = casa(piano, den, mq) 
                self.condomini[con].aggiungiCasa(casa(piano, den, mq))

            # ora ho messo in quartiere tutti i condomini del .csv 
            # e tutte le case divise per conominio         







        






