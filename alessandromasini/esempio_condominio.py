# definire la classe CASA

class casa:
    def __init__(self, piano, denominazione, mq):

        self.piano = piano
        self.denominazione = denominazione
        self.mq = mq

class attico(casa):

    def __init__(self, piano, denominazione, mq, mqterrazzo):

        casa.__init__(piano, denominazione, mq)
        self.mqterrazzo = mqterrazzo

class condominio():

    def __init__(self):

        self.elencoCase = {} # qui dentro ci metto tutte le case
        self.totmq = 0

    def aggiungiCasa(self, c:casa):

        #devo vedere quanti mq aggiungo per completare mq del condominio
        casamq = c.mq
        denom = c.denominazione
        self.totmq += casamq

        self.elencoCase.append(c)
