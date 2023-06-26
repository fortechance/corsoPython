

from sqlalchemy import create_engine, ForeignKey, Column, CHAR, Float, Integer, String, MetaData, DateTime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from sqlalchemy import MetaData

from urllib.parse import quote

import datetime




dialect = "mysql"
user = "c73db"
password = "ocGB@QkcA8"
host = "python.hostingstudenti.fortechance.com"
schema = "c73db"
pwe = quote(password, safe ="")


conn = f"{dialect}://{user}:{pwe}@{host}/{schema}"

engine = create_engine(conn, echo = True)

#engine = create_engine(f"mysql://c73db:{pwe}@python.hostingstudenti.fortechance.com/c73db")

Base = declarative_base()


#definire le classi python che poi andranno nel database

#causali:

class causale(Base):

    __tablename__ = "causali"

    codcausale = Column(String(5), primary_key=True)
    descrizione = Column(String(50))
    segno = Column(CHAR)

    def __init__(self, codc, desc, segno):

        self.codcausale = codc
        self.descrizione = desc
        self.segno = segno

    def __repr__(self):

        ret = f"{self.codcausale} {self.descrizione} {self.segno}"
        return ret
    

class tipowallet(Base):

    __tablename__ = "tipi wallet"

    codtipowallet = Column(String(5), primary_key=True)
    descrizione = Column(String(50))

    def __init__(self, cod, descr):

        self.codTipoWallet = cod
        self.descrizione = descr

    def __repr__(self):

        ret = f"{self.codTipoWallet} {self.descrizione}"
        return ret
    

class utente(Base):

    __tablename__ = "utenti"

    codutente = Column(String(5), primary_key=True)
    nome = Column(String(25))
    cognome = Column(String(25))

    def __init__(self, cod, nome, cognome):

        self.codutente = cod
        self.nome = nome
        self.cognome = cognome

    def __repr__(self):

        ret = f"{self.codutente} {self.nome} {self.cognome}"
        return ret
    
#entita' deboli

class movimento(Base):

    __tablename__ = "movimenti"

    id = Column(Integer,autoincrement="auto", primary_key=True)
    importo = Column(Float)
    descrizione = Column(String(50))
    dtmovimento = Column(DateTime)
    codCausale = Column(String(5), ForeignKey("causali.codcausale"))
    
    def __init__(self, codcausale, importo):

        self.importo = importo
        self.codCausale = codcausale
        self.dtmovimento = datetime.datetime.now()
        self.id = id 

    def __repr__(self):

        ret = f"{self.id} {self.codCausale} {self.importo} {self.dtmovimento}"
        return ret

metobj = MetaData()

MetaData().create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()




