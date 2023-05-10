class utente():
    def __init__(self):
        pass

class tipoWallet():
    def __init__(self):
        pass

class wallet():
    def __init__(self, u:utente, tw:tipoWallet):

        self.movimenti = {}
        self.utente = u
        self.tipowallet = tw
        pass

class causale():
    def __init__(self):
        pass
class movimento():
    def __init__(self,c:causale):
        self.causale = c
        pass

class bottino():
    def __init__(self):

        self.wallets = {}

        def addWallet(w:wallet):
            wallets[w] = w
