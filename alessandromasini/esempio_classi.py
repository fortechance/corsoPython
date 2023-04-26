# classi

class questionario():

    #costruttore
    def __init__(self):

        self.nome = ''
        self.cognome = '' 



######################## programma ############################

questy = questionario()
pippo = questionario()

pippo.cognome = 'Bianchi'
pippo.nome = 'Luigi'

questy.cognome = 'Rossi'
questy.nome = 'Mario'

a = []
b = questionario()

a.append(b)

a[0].cognome = 'Verdi'
a[0].nome = 'Giuseppe'

print(a[0].cognome)
print(questy.cognome)
print(pippo.cognome)

