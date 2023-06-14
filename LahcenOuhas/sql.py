from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  MetaData
# Create a base class
Base = declarative_base()
# Define a class representing a table
class causale(Base):
  __tablename__ = 'causale'
  CODCAUSALE=Column(Integer(5),primary_key=True)
  descausale = Column(String(50))
  segnocausale = Column(String(7))

  host="python.hostingstudenti.fortechance.com"
  user="c73db"
  passw="ocGB@QkcA8"
  schema="c73db"
  dialect= "mysql"
  conn= f'{dialect}://{user}:{passw}@{host}/{schema}'
  engine= create_engine(conn)
# Create the tables in the database
  MetaData.create_all(engine)
# Create a metadata object
  MetaData().create_all(bind=engine)
# Create a session factory
  Session=sessionmaker(bind=engine)
# Create a session
  session= Session()






# Create an engine and connect to a database
#engine= create_engine('mysql://c73db:ocGB@QkcA8@python.hostingstudenti.fortechance.com/schema')

#from urllib.parse import quote
#pw='ocGB@QkcA8'

#pwe=quote(pw,safe="")

#engine=create_engine(f'mysql://vc73db:{pwe}@python.hostingstudenti.fortechance.com/schema)'

