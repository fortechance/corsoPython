from myEngine import engine
from sqlalchemy import Table 
from sqlalchemy import Column,MetaData , ForeignKey
from sqlalchemy import Integer, String, CHAR, Numeric,DateTime

metaobj = MetaData()

user = Table(
    'users',
    metaobj,
    Column('ID', Integer, primary_key = True ),
    Column('nome', String(25)),
    Column('cognome', String(25)),
    Column('username',String(25)),
    Column('password', String(25))
    )

causale = Table(
    'causali',
    metaobj,
    Column('codice', String(5), primary_key = True),
    Column('descrizione', String(25)),
    Column('segno', CHAR)
)

movimento = Table(
    'movimenti',
    metaobj,
    Column('id',Integer, primary_key=True),
    Column('importo',Numeric(10,2) ),
    Column('dtMovimento', DateTime),
    Column('codcausale', String(5), ForeignKey('causali.codice'))
)

