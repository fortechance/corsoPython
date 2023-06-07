from sqlalchemy import create_engine, Column, Integer, String, DateTime, Row, MetaData
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
    codCau = Column(Integer(5), primary_key=True, autoincrement='auto')
    descrizioneCau = Column(String(50))
    segnoCau = Column(String(1))

