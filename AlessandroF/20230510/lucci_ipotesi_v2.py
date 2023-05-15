# ipotesi post progettazione di gruppo
# si è deciso dopo la discussione di inserire l'elemento wallet, il tipo wallet e di associare il segno 
# delle operazioni alla causale e non al movimento singolo.
# Avevo previsto l'accumulo come caratteristica dei obj_movimento ma durante la discussione si è deciso che
# basterà spsotare i fondi tra wallet
# Di seguito l'ipotesi 2:

##############
#CLASSI FORTI#
##############

class utente():
    def __init__(self, id_utente, nome_utente):

        self.id_utente = id_utente
        self.nom_utente = nome_utente


class causale():
    def __init__(self, id_causale, descrizione_causale, segno_causale):

        self.id_causale = id_causale
        self.descrizione_causale = descrizione_causale
        self.segno_causale = segno_causale

class tipo_wallet():
    def __init__(self, id_tipowallet, descrizione_tipowallet):

        self.id_tipowallet = id_tipowallet
        self.descrizione_tipowallet = descrizione_tipowallet

###############
#CLASSI DEBOLI#
###############

class wallet():
    def __init__(self, id_wallet, nome_wallet, descrizione_wallet):

        self.id_wallet = id_wallet
        self.nome_wallet = nome_wallet
        self.descrizione_wallet = descrizione_wallet

class obj_movimento():
    def __init__(self, nome, ricorrenza, causale, metodopagamento, importo):

        self.nome = nome   #nome del movimento
        self.ricorrenza = ricorrenza #se il movimento è ricorrente o non nei mesi. Se ricorrente n° ricorrenze
        self.causale = causale  #categoria del movimento possiam aggiungere sotto categoria
        self.metodopagamanto = metodopagamento  #metodo del magamento del movimento
        #self.accumulo = accumulo  #se il movimento è in accumulo o un residuo a scadenza Può valere anche per i buoni pasto
        self.importo = int(importo) #importo del movimento espresso come numero sarebbe da mettere almeno due virgole


############
#aggiuntivi#
############

class profiloutente():
    def __init__(self, id_profilouteente, categoriadipersona, animali, impiego):

        self.id_profilouteente = id_profilouteente
        self.categoriadipersona = categoriadipersona
        self.animali = animali
        self.impiego = impiego

class obiettivorisparmio():
    def __init__(self, nome, importo):

        self.nome = nome
        self.importo = importo

##############
#oggettifigli#
##############

class ricorrenza():
    def __init__(self, numeroricorrenze):

        self.numeroricorrenze = numeroricorrenze


        