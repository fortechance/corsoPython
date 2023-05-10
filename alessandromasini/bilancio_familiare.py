
class entrate():

    def __init__(self, emolumenti, assegno_unico, competenze):

        self.emolumenti = emolumenti
        self.assegno_unico = assegno_unico
        self.competenze = competenze
        self.totale_in = []
    
    def aggiungi_entrata(self, entrata):

        self.totale_in.append(entrata)

    def calcolo_entrate(self):

        totale = 0
        for i in self.totale_in:
            totale += i

        return totale
    



class uscite():

    def __init__(self, mutuo, bollette, tasse):

        self.mutuo = mutuo
        self.bollette = bollette
        self.tasse = tasse
        self.totale_out = []

    def aggiungi_uscita(self, uscita):

        self.totale_out.append(uscita)
    
    def calcolo_uscite(self):

        totale = 0
        for i in self.totale_in:
            totale += i
            
        return totale




class risparmio():

    def __init__(self, obbiettivo):

        self.obbiettivo = obbiettivo



    def rimanenza(self):

        rimane = self.entrata - self.uscita
        return rimane
    
    def calcolo_entrate(self):

        pass

 