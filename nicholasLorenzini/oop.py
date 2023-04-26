#classi, istanze ecc.
#definisco la classe
"""
class questionario():
    #costruttore. Parola chiave self, serve per richiamare la classe
    def __init__(self):
        self.nome = ""
        self.cognome = ""


#istanza
questy = questionario()
questy2 = questionario()

questy.nome = "Pippo"
questy.cognome = "Pluto"

questy2.nome = "Pietro"
questy2.cognome = "Pietra"

#lista vuota
a = []
#creo istanza questionario
b = questionario()
#a[0] aggiungo un elemento con append, in questo caso una classe
a.append(b)

c = questionario()
#a[1]
a.append(c)

a[0].nome = "nelNome"
a[0].cognome = "delSignore"
a[1].nome = "qualeNome"
a[1].cognome = "delSignore"
"""
########## es2 ########

class professione():
    #costruttore. Parola chiave self, serve per richiamare la classe
    def __init__(self):
        self.tipoLavoro = ""
        self.attiva = True

class anagrafica():
    #costruttore. Parola chiave self, serve per richiamare la classe
    def __init__(self,prof):
        self.nome = ""
        self.cognome = ""
        #considera questo valore come se fosse una professione
        self.pro:professione = prof
        
lista = []
lavoro = professione()
lavoro.tipoLavoro = "Falegname"

persona = anagrafica(lavoro)

lista.append(persona)
lista[0].nome = "Nome"
lista[0].cognome = "Cognome"
lista[0].tipoLavoro = lavoro.tipoLavoro

print(lista[0].tipoLavoro)
