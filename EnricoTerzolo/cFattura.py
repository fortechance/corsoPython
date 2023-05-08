# altra definizione di classi

import datetime

class cliente():

    def __init__(self, denominazione, piva, cfisc, modpag, sconto):
        
        self.denominazione = denominazione
        self.piva = piva
        self.codfiscale = cfisc
        self.modpag = modpag
        self.sconto = sconto
        self.codcliente = self.denominazione[0,3]
        
        msec = datetime.datetime.microsecond
        self.codcliente += str(msec)

class articolo():

    def __init__(self, codart, denominazione, prezzo, iva, umisu):

        self.codart = codart
        self.denominazione = denominazione
        self.prezzo = prezzo
        self.iva = int(iva)
        self.umisu = umisu

        #operazioni di controllo ....

class dettagliofattura():

    def __init__(self, art:articolo, qta, sconto):

        self.articolo = art
        self.qta = qta
        self.sconto = sconto

class fattura():

    def __init__(self,cli:cliente, num, data, sconto):

        self.dettaglio = []
        self.cliente = cli
        self.numFattura = int(num)
        self.dataFattura = data

    def aggiungiRiga(self, dett:dettagliofattura):

        self.dettaglio.append(dett)
        

