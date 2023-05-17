# definisco le classi per il programma di gestione spese/entrate

import datetime import d

class impiego():                        # definisco la classe della situazione lavorativa

    def __init__(self, sit_lav):
       
       self.sit_lav = sit_lav

class profilatura():                         # definisco la classe della situazione familiare

    def __init__(self, profil):
       
       self.profil = profil

class utente():                         # definisco la classe dei nominativi 

    def __init__(self, nome, cognome, data_nascita, luogo_nascita, cod_fisc, indirizzo, n_civico, CAP, citta, sit_lav:impiego, profil:profilatura):
        
        self.nome = nome
        self.cognome = cognome
        self.
        self.impiego = sit_lav
        self.profilatura= profil

class tipo_entrata():                        # definisco la classe della tipologia entrate
    
    def __init__(self, tip_ent):
       
       self.tip_ent = tip_ent

class entrate():                        # definisco la classe delle entrate                      
    
    def __init__(self, data, importo, tip_ent: tipo_entrata):

        self.data_entrata = data
        self.importo = importo
        self.tipo_entrata = tip_ent

class tipo_uscita():                        # definisco la classe della tipologia uscita
    
    def __init__(self, tip_usc):
       
       self.tip_usc = tip_usc

class modalita_pagamento():                        # definisco la classe della modalità di pagamento
    
    def __init__(self, mod_pag):
       
       self.mod_pag = mod_pag
 
class uscite():                         # definisco la classe delle uscite                      
    
    def __init__(self, data, importo, tip_usc: tipo_uscita, mod_pag: modalita_pagamento):

        self.data_uscita = data
        self.importo = importo
        self.tipo_uscita = tip_usc
        self.modalita_pagamento = mod_pag

class tipo_investimento():                        # definisco la classe della tipologia di investimento
    
    def __init__(self, tip_inv):
       
       self.tip_inv = tip_inv

class investimenti():                   # definisco la classe degli investimenti                     
    
    def __init__(self, data, importo, tip_inv: tipo_investimento):

        self.data_uscita = data
        self.importo = importo
        self.tipo_investimento = tip_inv