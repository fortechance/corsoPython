from classiWallet import *

Causali = {}
Utenti = {}
TipoWallet = {}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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

eCau = causali()

try:
    c = causale('stipendio','+')
    eCau.AddCausale(c)
    c = causale('Mutuo','-')
    eCau.AddCausale(c)
    #questo genera un errore:
    c= causale('lotteria', '+')
    eCau.AddCausale(c)
    c= causale('Riscossione Affitto', '+')
    eCau.AddCausale(c)

except:
    print(f'causale {c.descrizione} duplicata')

try:

    cc = causale('Stipendio','+')
    m=movimento(cc,2000,eCau)
    
except:
    print(f'causale {cc.descrizione} non esiste')


