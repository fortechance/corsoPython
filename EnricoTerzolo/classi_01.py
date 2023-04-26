# classi, istanze e qunt'altro

class professione():

    def __init__(self):
        self.impiego = ""
        self.stabile = True

class questionario():

    #costruttore
    def __init__(self,prof):

        self.ddnomen = ''
        self.cognome = ''
        self.pro:professione = prof
        self.eta = 0

########################## programma ######################


chefaccio = professione()

chisono = questionario(professione)

chisono.cognome = "Rossi"
chisono.nome = 'Mario'

chisono.pro.impiego = 'operaio'
chisono.pro.stabile =True    
chisono.eta = 54

print(chisono.cognome) 
print(chisono.ddnomen) 
print(chisono.pro.impiego) 
print(chisono.pro.stabile) 

dict= {}

dict['chiave'] ={}

dict["chiave"]['cognome'] = 'Rossi'
dict["chiave"]['nome'] = 'Mario'
dict["chiave"]['eta'] = 54
dict["chiave"]['pro'] = {}
dict['chiave']['pro']['impiego'] = 'operaio'
dict['chiave']['pro']['stabile'] = True