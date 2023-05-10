# definisco le classi per il programma di gestione spese/entrate

from datetime import datetime

class impiego():                        # definisco la classe della situazione lavorativa

    def __init__(self, sit_lav):
       
       self.sit_lav = sit_lav

class profilatura():                    # definisco la classe della situazione familiare

    def __init__(self, profil):
       
       self.profil = profil

class utente():                         # definisco la classe degli utenti

    def __init__(self, nome, cognome, data_nascita, luogo_nascita, cod_fisc, indirizzo, n_civico, CAP, prov, citta, sit_lav:impiego, profil:profilatura):
        
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.cod_fisc = cod_fisc
        self.indirizzo = indirizzo
        self.n_civico = n_civico
        self.CAP = CAP
        self.citta = citta
        self.prov = prov
        self.impiego = sit_lav
        self.profilatura= profil

class tipo_wallet():                        # definisco la classe della tipologia wallett (c/c, conto risparmio, ecc.)
    
    def __init__(self, tip_wal):
       
       self.tip_wal = tip_wal

class causale():                            # definisco la classe delle causali movimenti, con entrata/uscita                  
    
    def __init__(self, causale, segno):

        self.causale = causale
        self.segno = segno

class movimento():                          # definisco la classe dei movimenti finanziari
    
    def __init__(self, datetime, importo, causale: tipo_movimento, da_dove, a_dove):

        
 
