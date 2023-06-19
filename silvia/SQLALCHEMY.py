#SQLALCHEMY 

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData


base = declarative_base

class Causale (base):
    __tablename__='causali'
    codcausale = Column(String(5), primary_key=True)
    desccausale = Column(String(50))
    segnocausale = Column(String(7))


host = 'python.hostingstudenti.fortechance.com'
dialect = 'mysql'
user = 'c73db'
schema = 'c73db'
password = 'ocGB@kcA8'

conn= f'{dialect}://{user}:{password}@{host}/{schema}'
engine = create_engine (conn)


MetaData.create_all(engine)

Session= sessionmaker(bind=engine)

session = Session()







