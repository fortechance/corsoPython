

class utente():

    def __init__(self, nome, cognome):

        self.nome = nome
        self.cognome = cognome
        


class causali():

    def __init__(self, descrizione):

        self.descrizione = descrizione



class tipo_wallet():

    def __init__(self, tipo):

        self.tipo = tipo
        



class wallet():

    def __init__(self, numeroconto):

        self.numeroconto = numeroconto
        self.totale = []



class movimento(wallet):

    def __init__(self, data, segno):
        wallet.__init__(numeroconto)

        self.data = data
        self.segno = segno

    def aggiungi_movimento(self, mov):

        self.totale.append(mov)

    def calcolo_entrate(self):

        totale = 0
        for i in self.totale:
            totale += i

        return totale





