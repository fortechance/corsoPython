class Utente():

    def __init__(self, nome, cognome, data_di_nascita, professione):
        self.nome = nome
        self.cognome = cognome
        self.data = data_di_nascita
        self.professione = professione


class Causale():

    def __init__(self, segno, descrizione):
        self.segno = segno
        self.descrizione = descrizione

class Movimenti():

    def __init__(self, data, importo, causale: Causale, ccprovenienza, ccdestinazione):
        self.data = data
        self.importo = importo
        self.causale = causale
        self.ccprovenienza = ccprovenienza
        self.ccdestinazione = ccdestinazione #opzionale, solo in caso di trasferimenti interni

class Wallets():

    class ContoCorrente_Principale():

        def __init__(self, movimenti: Movimenti, saldo):
            self.movimenti = movimenti
            self.saldo = saldo
            
    class ContoCorrente_Risparmio():

        def __init__(self, movimenti: Movimenti, saldo):
            self.movimenti = movimenti
            self.saldo = saldo
    
    class BuoniPasto():

        def __init__(self, data, segno, unita, importo_unitario, saldo):
            self.data = data
            self.segno = segno
            self.unita = unita
            self.importo = importo_unitario
            self.ctvt= self.unita * self.importo
            self.saldo = saldo

    class DepositoTitoli():

        def __init__(self, movimenti: Movimenti, saldo):
            self.movimenti = movimenti
            self.saldo = saldo
    
    class CartaDiCredito():

        def __init__(self, movimenti: Movimenti, saldo):
            self.movimenti = movimenti
            self.saldo = saldo
    
    class BuonoCeliachia():

        def __init__(self, movimenti: Movimenti, saldo):
            self.movimenti = movimenti
            self.saldo = saldo

class EstrattoContoMensile():

    def __init__(self, saldo):
        self.saldo_cc_principale = saldo #vedere come completare

