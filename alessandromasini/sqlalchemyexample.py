

from sqlalchemy import create_engine, Column, Integer, String, DateTime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from sqlalchemy import MetaData

from urllib.parse import quote




dialect = "mysql"
user = "c73db"
password = "ocGB@QkcA8"
host = "python.hostingstudenti.fortechance.com"
schema = "c73db"
pwe = quote(password, safe ="")


conn = f"{dialect}://{user}:{pwe}@{host}/{schema}"

engine = create_engine(conn)

#engine = create_engine(f"mysql://c73db:{pwe}@python.hostingstudenti.fortechance.com/c73db")

Base = declarative_base()

class Causale(Base):
    __tablename__ = "causali"
    codcausale = Column(String(5), primary_key=True)
    descrizione = Column(String(50))
    segnocausale = Column(String(1))

MetaData().create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()




