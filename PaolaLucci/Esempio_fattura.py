import datetime

class Cliente():

    def __init__(self, denominazione, piva, cfiscale, modpag, sconto):
        
        self.denominazione = denominazione
        self.piva= piva
        self.cfiscale = cfiscale
        self.modpag = modpag
        self.sconto = sconto
        self.codcliente = self.denominazione[0, 3]
        
        msec = datetime.datetime.microsecond
        self.codcliente += str(msec)


class Articolo():

    def __init__(self, codart, denominazione, prezzo, iva, unitamisura):

        self.codart = codart
        self.denominazione = denominazione
        self.prezzo = prezzo
        self.iva = int(iva)
        self.unitamisura = unitamisura

class DettaglioFattura():

    def __init__(self, art: Articolo, qta):

        self.Articolo = art
        self.qta = qta
        self.sconto = sconto
        
class Fattura():

    def __init__(self, clt: Cliente, numero, data, sconto):

        
        self.dettaglio = []
        self.cliente = clt
        self.numFattura = int(numero)
        self.dataFattura = data
        self.sconto = sconto

    def AggiungiRiga(self, dett:DettaglioFattura):
        self.dettaglio.append(dett)
