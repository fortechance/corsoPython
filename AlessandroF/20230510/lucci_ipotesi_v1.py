# ipotesi post progettazione di gruppo
#Avevo considerato come oggetto prinvipale l'oggettomovimento senza pensare al wallet
#ma più o meno tutti i parametri necessari li avevo ipotizzati associandoli alla class obj_movimento

###OGGETTI PRINCIPALI

class obj_movimento():
    def __init__(self, nome, in_out, ricorrenza, categoria, metodopagamento, accumulo, importo):

        self.nome = nome   #nome del movimento
        self.in_out = in_out  #se il movimento è un attivo o un passivo
        self.ricorrenza = ricorrenza #se il movimento è ricorrente o non nei mesi. Se ricorrente n° ricorrenze
        self.categoria = categoria  #categoria del movimento possiam aggiungere sotto categoria
        self.metodopagamanto = metodopagamento  #metodo del magamento del movimento
        self.accumulo = accumulo  #se il movimento è in accumulo o un residuo a scadenza Può valere anche per i buoni pasto
        self.importo = int(importo) #importo del movimento espresso come numero sarebbe da mettere almeno due virgole

class profiloutente():
    def __init__(self, categoriadipersona, animali, impiego):

        self.categoriadipersona = categoriadipersona
        self.animali = animali
        self.impiego = impiego

class obiettivorisparmio():
    def __init__(self, nome, importo):

        self.nome = nome
        self.importo = importo

########OGGETTI FIGLI

class ricorrenza():
    def __init__(self, numeroricorrenze):
        
        self.numeroricorrenze = numeroricorrenze


        