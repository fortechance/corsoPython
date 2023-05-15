import datetime as dt

today = dt.date()
print (today)

class Utente():
    def __init__(self, nome, cognome, dataN, indirizzo, citta, CAP, impiego) -> None:
        self.nomeU = nome
        self.cognome = cognome
        self.dataN = dataN
        self.indirizzo = f"{indirizzo}, {citta}, {CAP}"
        self.impiego = impiego
        animali = []
        
    def calcEta(dataN):
        today = dt.today()
        return today.year - dataN.year - ((today.month, today.day) < (dataN.month, dataN.day))