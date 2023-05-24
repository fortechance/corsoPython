class utente():
    def __init__(self, codice, nome, cognome):

        self.codice = codice
        self.cognome = cognome
        self.nome = nome

class tipoWallet():
    def __init__(self, codice, descrizione, reale):
        
        self.codice = codice
        self.descrizione = descrizione
        self.tipo = reale
 
class wallet():
    def __init__(self, tw:tipoWallet, nome, codice):

        self.movimenti = {}
        self.tipowallet = tw
        self.walletName = nome
        self.codicewallet = codice
        self.saldo = 0

class causale():
    def __init__(self, codice, descrizione, segno):
        
        self.codicd = codice
        self.descrizione = descrizione
        self.segno = '+' if segno == '+' else '-'

class causali():

    def __init__(self):

        self.elencoCausali = {}

    def AddCausale(self, c:causale):

        if self.CausaleExist(c):
            raise Exception('Causale Duplicata')
        else:
            self.elencoCausali[c.codice] = c
    
    def CausaleExist(self, c:causale):

        if c.codice in self.elencoCausali.keys():
            return True
        else:
            return False
        
class movimento():
    def __init__(self,c:causale, importo, elencoCau:causali):
        
        if (elencoCau.CausaleExist(c)):

            self.causale = c
            self.importo = importo
    
        else:
            raise Exception(f'causale {c.descrizione} inesistente')

class portfolio():
    def __init__(self, u:utente):

        self.utente = u
        self.wallets = {}

    def addWallet(self, w:wallet):
        self.wallets[w.walletName] = w
