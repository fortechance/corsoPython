from classiWallet import *
from login_paola import *
from portfolio import *

import os

Causali = {}
Utenti = {}
TipoWallet = {}
Logins = {}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
pass
def initLogins(fileName):

    file = BASE_DIR + '\\' + fileName
    
    with open(file,'r') as f:
        dati = f.read()

    righe = dati.split('\n')
    nriga =0

    for riga in righe:
        if (nriga == 0):
            nriga +=1
            continue

        colonne = riga.split(';')
        #ora bbiamo le colonne suddivise riga per riga

        username = colonne[0]
        password = colonne[1]
        codiceUtente = colonne[2]

        #lo aggiungo al dizionario

        l = {}
        l['username'] = username
        l['password'] = password
        l['codiceutente'] = codiceUtente

        Logins[username] = l


def initTipoWallet(fileName):

    file = BASE_DIR + '\\' + fileName
    
    with open(file,'r') as f:
        dati = f.read()

    righe = dati.split('\n')
    nriga =0

    for riga in righe:
        if (nriga == 0):
            nriga +=1
            continue

        colonne = riga.split(';')
        #ora bbiamo le colonne suddivise riga per riga

        codice = colonne[0]
        descrizione = colonne[1]
        tipo = colonne[2]

        #lo aggiungo al dizionario

        w = {}
        w['Descrizione'] = descrizione
        w['Tipo'] = tipo

        TipoWallet[codice] = w

def initCausali(fileName):

    file = BASE_DIR + '\\' + fileName
    
    with open(file,'r') as f:
        dati = f.read()

    righe = dati.split('\n')
    nriga =0

    for riga in righe:
        if (nriga == 0):
            nriga +=1
            continue

        colonne = riga.split(';')
        #ora bbiamo le colonne suddivise riga per riga

        codice = colonne[0]
        descrizione = colonne[1]
        segno = colonne[2]

        #lo aggiungo al dizionario

        c = {}
        c['Descrizione'] = descrizione
        c['Segno'] = segno

        Causali[codice] = c


def initUtenti(fileName):

    file = BASE_DIR + '\\' + fileName
    
    with open(file,'r') as f:
        dati = f.read()

    righe = dati.split('\n')
    nriga =0

    for riga in righe:
        if (nriga == 0):
            nriga +=1
            continue

        colonne = riga.split(';')
        #ora bbiamo le colonne suddivise riga per riga

        codice = colonne[0]
        cognome = colonne[2]
        nome = colonne[1]

        #lo aggiungo al dizionario

        u = {}
        u['Cognome'] = cognome
        u['Nome'] = nome

        Utenti[codice] = u

initTipoWallet('0_tipowallet.csv')
initCausali('0_causali.csv')
initUtenti('0_utenti.csv')
initLogins('0_login.csv')

# adesso abbiamo letto tutti i csv con i dati di base

# forniamo una videata di login e verifichiamo che sia ok
user, passw = doLogin()
loginok = False

# identifico se c'è l'utente segnato dal login
if (user in Logins.keys()):
    if (Logins[user]['password'] == passw):
        #login corretto
        #recupero dati utente.
        cod = Logins[user]['codiceutente']
        uOK = Utenti[cod]
        print(uOK)
        loginok = True

    else:
        print('passsword errata')
else:
    print('user errato')

#adesso creo la classe utente con i dati di login
if loginok:
    u = utente(cod,uOK['Nome'], uOK['Cognome'])
    # creo il portfolio dell'utente
    por = portfolio(u)

else:
    print('Login Fallito')
    raise Exception ('Login Fallito') 
# login ok, portfolio creato

showPortfolio(por)





          



