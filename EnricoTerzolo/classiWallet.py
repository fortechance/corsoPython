class utente():
    def __init__(self, cognome, nome, indirizzo, citta,procincia):
        pass

class tipoWallet():
    def __init__(self, descrizione, reale):
        pass

class wallet():
    def __init__(self, u:utente, tw:tipoWallet, nome):

        self.movimenti = {}
        self.utente = u
        self.tipowallet = tw
        self.walletName = nome
        self.saldo = 0

        pass

class causale():
    def __init__(self, descrizione, segno):
        self.descrizione = descrizione
        self.segno = '+' if segno == '+' else '-'

class causali():

    def __init__(self):

        self.elencoCausali = {}

    def AddCausale(self, c:causale):

        if self.CausaleExist(c.descrizione):
            raise Exception('Causale Duplicata')
        else:
            self.elencoCausali[c.descrizione] = c
    
    def CausaleExist(self, descrizione):

        if descrizione in self.elencoCausali.keys():
            return True
        else:
            return False
        
class movimento():
    def __init__(self,c:causale, importo, elencoCau):
        
        if (c.descrizione in elencoCau.elencoCausali.keys()):

            self.causale = c
            self.importo = importo
    
            if (c.segno == '-'):
                self.importo = self.importo * -1
        else:
            raise Exception(f'causale {c.descrizione} inesistente')

        

class bottino():
    def __init__(self):

        self.wallets = {}

        def addWallet(w:wallet):
            self.wallets[w.walletName] = w
