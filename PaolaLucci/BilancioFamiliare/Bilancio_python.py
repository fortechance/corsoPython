class questionario():

    # costruttore
    def __init__(self):

        self.name = ''
        self.cognome = ''

questy = questionario()
# questy diventa l'istanza della classe questionario, con tutte le caratteristiche definite al suo interno

questy.cognome = 'Rossi'
questy.nome = 'Paolo'

case = questionario()
# a partire dalla stessa classe questionario posso creare un'altra istanza dello stesso tipo, che identificano due
# categorie separate, ma che utilizzano  gli stessi dati di partenza, in questo caso nome e cognome

case.nome = 'Francesco'
case.cognome = 'Bianchi'

a = []
b = questionario()

a.append(b)

a[0].cognome = 'Verdi'
a[0].nome = 'Giuseppe'

print(a[0].cognome)
print(questy.cognome)
print(case.cognome)