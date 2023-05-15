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
    
            if (c.segno == '-'):
                self.importo = self.importo * -1
        else:
            raise Exception(f'causale {c.descrizione} inesistente')

class bottino():
    def __init__(self):

        self.wallets = {}

    def InitEntitaForti(self, fileCausali, fileUtenti, fileTipoWallet):
        #devo leggere i CSV, poi devo metterli nel db
        pass

    def addWallet(self, w:wallet):
        self.wallets[w.walletName] = w
