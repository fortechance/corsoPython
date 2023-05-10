#classificazione 2 bilancio familiare

from typing import Any


class Utente():
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome 
        self.username = self.nome [0,2]+ self.cognome[0,2]


class TipoWallet():
    def __init__(self, CC, DT, prepagata, welfare, buonipasto, gaming):
        self.CC = CC
        self.DT = DT
        self.prepagata = prepagata
        self.welfare = welfare
        self.buonipasto = buonipasto 
        self.gaming = gaming

class Causale():
    def __init__(self, entrata, uscita, trasferimento):
        self.entrata = entrata
        self.uscita = uscita
        self.trasferimento = trasferimento
