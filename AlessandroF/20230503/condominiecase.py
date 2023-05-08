# definire la classe casa
class casa():      #la class casa avrà un costruttore che avrà come parametro self, piano , denominazione ....)

    def __init__(self, piano, denominazione, mq):
        #inizializziamo (rendiamo pubbliche all'istanza)
        self.piano = piano
        self.denominazione = denominazione
        self.mq = int(mq)

#ora voglio attico che eredita da casa:
class attico(casa):

    def __init__(self, piano, denominazione, mq, mqterrazzo):

        casa.__init__(piano, denominazione, mq)  #chiamo il costruttore di casa che tanto ho ereditato 
        self.mqterrazzo = mqterrazzo           # in più gli carico qualcosa di esxclusivo (mqterrazzo)

class condominio():

    def __init__(self, nome):
        #il mio costruttore vorrà un elenco come lista
        self.elencoCase = {} #qui dentro ci metto tutte le case componenti il condominio
        #devo vedere quanti mqaggiungo per completare i tot mq delcondominio
        self.totmq = 0
        self.nomecondominio = nome #questo è il nome del condominio preso dal file csv

    def aggiungiCasa(self, c:casa):    #dato che non so se si aggiunge una casa o un condominio facciamo che c me lo aggiungi come "casa" scrivo c:casa come se mi aspettassil'oggetto c che verrà passato come se fosse un oggetto casa
        #così ci suggerisce o propone i valori del tipo casa
        #devo vedere quanti mqaggiungo per completare i tot mq delcondominio 
        casamq = c.mq
        denom = c.denominazione
        
        try:
            self.elencoCase[denom] = c
            self.totmq += int(casamq)
        except:
            pass 


        #l'elenco delle caseè 
        #il singolo appartamaneto avrendo una chiave può essere inserito nel dizionario (a patto che non vi siano denominazoini uguali l'una all'altra=)

    def calcolaMillesimi(self, denominazione):

        mq = self.elencoCase[denominazione].mq
        millesimi = 1000*mq/self.totmq      #calcolo i millesimi

        return millesimi  #mi faccio restituire i millesimi
    
#fino a qui ho solo descritto la struttura di ciò che mi interessa.
#non abbiamo scritto nulla , ZERO di codice

class quartiere():

    def __init__(self, csvCondominio):

        #leggo ilfile csv. Chiamo "f" il file letto.
        #Ho vari modi per leggerlo ne elenco due:

        #1) esempio di lettura NON ATOMICA (ovvero NON divisibile, quindi non la usiamo)

 #       f = open(csvCondominio, 'r')
 #       buffer = f.read()
 #       f.close() #dato che il file viene chiuso nel terzo STEP se qualcosa andasse male nel primo step il file rimarrebbe aperto

        #2) apro il file e lo leggo finchè è aperto poi termino il tutto ed il file è chiuso in automatico
        self.condomini = {}
        with open(csvCondominio) as f:
            buffer = f.read ()
########################
#leggiamo il file csv le cui righe sono separate da CR/LF (carriage return / line feed come si faceva con la macchina da scrivere)
#i campi sono separati da 
            appartamenti = buffer.split('\n')
            #per ogni riga che c'è in appartamenti
            for app in appartamenti:
                #smonto il contenuto di ogni riga e lo metto dentro "dati" che è una lista di campi
                dati = app.split(';')
                #i campi che splitto saranno i seguenti:
                #dati[0] = idcondominio
                #dati[1] = piano
                #dati[2] = denominazione
                #dati[3] = mq

                con = dati[0]
                piano = dati[1]
                den = dati[2]
                mq = dati[3]
        #ora prendo questi dati e li inserisco nelle classi.
        #è ora di creare le istanze
                #se non esiste il condominio
                if ( con in self.condomini.keys()):
                    pass
                else:
                    #lo creo chiamandolo con il dato che ho letto:
                    self.condomini[con] = condominio(con)

                #adesso aggiungo la casa con gli altri dati che mi sono rimasti nella classe self.condomini
                #c = casa(piano, den, mq)
                self.condomini[con].aggiungiCasa(casa(piano, den, mq))
#ora ho messo in quartirere tutti i condomini del csv e tutte le case divise per condominio,
