from create_engine import engine

#qui facciamo le tabelle
from sqlalchemy import Table, Column, Integer, String, CHAR, MetaData

#per usare metadata devo fare oggetto metadata, che mi serve per tradurre in sql
metaobj = MetaData()

'''
tutte le tabelle da creare=classi da creare. convenzioni: tutto minuscolo. 
tabelle del database: con iniziale maiuscola

user = Table(
    'Users',
    metaobj,
    Column('ID',String(6)) 
    ecc....

nome dei campi: tutto maiuscolo
)
forti:
User:
    cod_utente  string(6), primary_key
    nome    string(25), not null (nella classe si rende con "nullable = False")
    cognome string(25), not null
    email   string(35), not null
    password    string(16), not null

TipoWallet:
    codice  string(3), primary_key
    descrizione string(25), not null
    tipo    string(25), not null

Causale:
    codice  string(3), primary_key
    descrizione string(25), not null
    segno    CHAR, not null

Wallet: #deve stare su un portfolio
    ID  integer, primary_key
    descrizione string(25), not null
    tipowallet  string(3), foreign_key(TipoWallet.codice) #ossia solo di un tipo che esiste nella tabella tipowallet
    fisicovirtuale  CHAR, not null
    idportfolio integer, foreign_key = (Portfolio.id)
    
deboli:
Movimento:
    ID  integer, primary_key
    importo numeric(10,2), not null
    causale string(3), foreign_key(Causale.codice) #ossia è ereditata da causale
    dtmovimento datetime, not null
    descrizione string(25)
    IDwallet    integer, foreign_key(Wallet.ID) #xk il movimento deve essere fatto su un wallet x frz

Portfolio
    id  integer, primary_key
    descrizione string(25)
    owner   codutente, string(6), foreign_key(Users.cod_utente)
'''

#creazione tabelle
user = Table(
    "users",
    metaobj, #gli dico che la classe deve metterla dentro il meteaoggetto definito sopra
    Column("ID", Integer, primary_key = True),
    Column("Nome", String(25)),
    Column("cognome", String(25)),
    Column("username", String(25)),
    Column("password", String(25))
)

causale = Table(
    "causali",
    metaobj,
    Column("ID", Integer, primary_key = True),
    Column("Descrizione", String(25)),
    Column("Segno", CHAR),
)

movimento = Table(
    "movimenti",
    metaobj,
    Column("ID", Integer, primary_key = True),
    Column("Importo", String(25)),
    Column("dtMovimento", DateTime),
    Column("codcausale", String(5), primary_key = ),
)
#NON è creazione di istanze, gli descrivo solo come sono fatte le mie classi