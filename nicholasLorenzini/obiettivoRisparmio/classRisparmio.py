import datetime as dt

class utente():
    def __init__(self, nome, cognome, dataN, indirizzo, citta, CAP, impiego):
        self.nomeU = nome
        self.cognome = cognome
        #regolo la data nel formato che voglio tramite la libreria datetime
        self.dataN = dt.date.strptime(dataN, "%d/%m/%Y").date()
        self.indirizzo = f"{indirizzo}, {citta}, {CAP}"
        self.impiego = impiego
        animali = []
        
    def calcEta(self):
        today = dt.date.today().strftime("%d/%m/%Y")
        delta = today - self.dataN
        eta = int(delta.days / 365.25)
        return eta

class tipoWallet():
    def __init__(self, descrizione, reale):
        self.descrizione = descrizione
        self.reale = reale

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
        #risparmio tempo per i controlli con questa formula (se positivo allora segno + altrimenti -)
        self.segno = '+' if segno == '+' else '-'

class causali():

    def __init__(self):

        self.elencoCausali = {}
    #aggiungo la causale passando come valore la cusale
    def AddCausale(self, c:causale):
        #verifico se la causale esiste. Se esite ricevo un'eccezione
        if self.CausaleExist(c.descrizione):
            raise Exception('Causale Duplicata')
        else:
            #se la causale no esiste aggiorno il dizionario elencoCausali inserendo come chiave la descrizione della causale
            self.elencoCausali[c.descrizione] = c
    
    def CausaleExist(self, c:causale):
        #verifico se la descrizione della causale è presente come chiave nel dizionario elencoCausali
        if c.descrizione in self.elencoCausali.keys():
            pass
        else:
            newCausale = input(f'causale {c.descrizione} inesistente. Vuoi crearla?')
            
            if (newCausale == "SI"):
                causali.AddCausale(c)
        
class movimento():
    def __init__(self,c:causale, importo, elencoCau:causali):
        
        if (elencoCau.CausaleExist(c)):
            #se la causale esiste la istanzio 
            self.causale = c
            self.importo = importo
            #se il segno della causale è meno lo moltiplico per -1 in modo che l'importo sia negativo
            if (c.segno == '-'):
                self.importo = self.importo * -1
        else:
            raise Exception(f'causale {c.descrizione} inesistente')
            

        

class bottino():
    def __init__(self):

        self.wallets = {}

        def addWallet(w:wallet):
            self.wallets[w.walletName] = w
