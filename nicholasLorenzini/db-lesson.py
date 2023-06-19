from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, Float, DateTime, Row, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

#dati per la connessione al db
dialect = 'mysql'
host = 'python.hostingstudenti.fortechance.com'
schema = 'c73db'
user = 'c73db'
password = 'ocGB@QkcA8'

#formato per connessione al db es mysql://nomeUtente:Password@nomeHost/schema
conn = f'{dialect}://{user}:{password}@{host}/{schema}'
#connessione al db
eng = create_engine(conn)

MetaData().create_all(bind=eng)
#creo la sessione per effettuare le operazione connettendomi al db conn
Session = sessionmaker(bind=eng)
session = Session()

class causale (base):
    __tablename__ = 'Causali'
    codCau = Column(Integer, primary_key=True, autoincrement='auto')
    descrizioneCau = Column(String(50))
    segnoCau = Column(String(1))

    def __init__(self, codCau, descrizioneCau, segnoCau):
        self.codiceCausale = codCau
        self.descrCausale = descrizioneCau
        self.segnoCausale = segnoCau
        
    def __repr__(self):
        ret = f'({self.codiceCausale}) {self.descrCausale} {self.segnoCausale}'
        return ret

class tipoWallet (base):
    __tablename__ = 'Tipi_wallet'
    idTipoWal = Column(Integer, primary_key=True, autoincrement='auto')
    descrizioneWal = Column(String(50))
    tipoWal = Column(String(25))

    def __init__(self, idTipoWal, descrizioneWal, tipoWal):
        self.codWallet = idTipoWal
        self.descrWallet = descrizioneWal
        self.tipoWallet = tipoWal
        
    def __repr__(self):
        ret = f'({self.codWallet}) {self.descrWallet} {self.tipoWallet}'
        return ret
        
class Utente (base):
    __tablename__ = 'Utenti'
    codUt = Column(Integer, primary_key=True, autoincrement='auto')
    nomeUt = Column(String(25))
    cognomeUt = Column(String(25))

    def __init__(self, codUt, nomeUt, cognomeUt):
        self.codUtente = codUt
        self.nomeUtente = nomeUt
        self.cognomeUtente = cognomeUt
        
    def inizialiUtente(self, nomeUt, cognomeUt):
        #self.inizialeNome = nomeUt[0]
        #self.inizialeCognome = cognomeUt[0]
        self.inizialeNome = "Nick"
        self.inizialeCognome = "Lore"
        
        self.iniziali = f'{self.inizialeCognome}{self.inizialeNome}'
        return self.iniziali
        
    def __repr__(self):
        ret = f'({self.codUtente}) {self.nomeUtente} {self.cognomeUtente}'
        return ret
