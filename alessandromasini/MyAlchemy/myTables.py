from myEngine import engine
from sqlalchemy import Table 
from sqlalchemy import Column,MetaData , ForeignKey
from sqlalchemy import Integer, String, CHAR, Numeric,DateTime

metaobj = MetaData()

'''
User:
    cod_utente  string(6), primary key 
    nome        string(25) not null
    cognome     string(25) not null
    email       string(35) not null
    password    string(16) not null

TipoWallet:
    codice      string(3), primary key
    descrizione string(25) not null
    Tipo        string(25) not null

Causale:
    codice      string(3), primary key
    descrizione string(25) not null
    segno       CHAR        not null

Portfolio:

    id          integer, primary key
    descrizione string(25)
    owner       codutente   string(6), foreign key (Users.cod_utente)

Wallet:

    ID          integer, primary key
    descrizione string(25) not null
    tipowallet  string(3), foreign key (TipoWallet.codice)
    fisicovirtuale  CHAR, not null
    idporfolio  integer, foreign key (Portfolio.id)

Movimento:

    ID          integer, primary key
    Importo     numeric(10,2) not null
    causale     string(3), foreign-key (Causale.codice)
    dtmovimento datetime, not null
    descrizione string(25)
    IDWallet    integer, foreign key(Wallet.ID)


'''

user = Table(
    'Users',
    metaobj,
    Column('COD_UTENTE', String(6), primary_key = True ),
    Column('NOME', String(25), nullable=False),
    Column('COGNOME', String(25), nullable = False),
    Column('EMAIL',String(35), nullable = False),
    Column('PASSWORD', String(16), nullable = False)
    )

tipowallet = Table(
    'TipoWallets',
    metaobj,
    Column('CODICE', String(3), primary_key=True),
    Column('DESCRIZIONE', String(25), nullable = False),
    Column('TIPO', String(25), nullable = False)

)

causale = Table(
    'Causali',
    metaobj,
    Column('CODICE', String(3), primary_key = True),
    Column('DESCRIZIONE', String(25), nullable = False),
    Column('SEGNO', CHAR, nullable = False)
)

portfolio = Table(
    'Portfolios',
    metaobj,
    Column('ID',Integer, primary_key=True),
    Column('DESCRIZIONE', String(25), nullable=False),
    Column('OWNER', String(6), ForeignKey('Users.COD_UTENTE'))

)

wallet = Table(
    'Wallets',
    metaobj,
    Column('ID', Integer, primary_key=True),
    Column('DESCRIZIONE', String(25), nullable=False),
    Column('TIPOWALLET', String(3), ForeignKey('TipoWallets.CODICE')),
    Column('FV' , CHAR,  nullable = False),
    Column('IDPORTFOLIO', Integer, ForeignKey('Portfolios.ID'))
)

movimento = Table(
    'Movimenti',
    metaobj,
    Column('ID',Integer, primary_key=True),
    Column('IMPORTO',Numeric(10,2) ),
    Column('CAUSALE', String(5), ForeignKey('Causali.CODICE')),
    Column('DTMOVIMENTO', DateTime, nullable = False),
    Column('DESCRIZIONE', String(25), nullable = False),
    Column('IDWALLET',Integer, ForeignKey('Wallets.ID') )
)

