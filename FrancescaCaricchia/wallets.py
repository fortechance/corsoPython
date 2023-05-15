class movimenti():
    def __init__(self, importo):
        self.importo = importo

class causali():
    def __init__(self, segno, descrizione):
        self.segno = segno
        self.descrizione = descrizione

class wallet()
    def __init__(self, mov:movimenti):
        self.movimenti = mov

class tipowallet():
    def __init__(self, wallet, tipologia):
        self.wallet = wallet
        self.tipologia = tipologia

class utente():
    def __init__(self, nome, wallet):
        self.nome = nome
        self.wallet = wallet

utente = dati("Francesca","wallet1")
tipowallet = tipo("wallet1", "conto")
wallet = wal(movimenti)
causali = caus("entrata","stipendio")
movimenti = movi("1000")