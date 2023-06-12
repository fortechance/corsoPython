from sqlalchemy import create_engine #very important from read out base data who we help us

from sqlalchemy.ext.declarative import declarative_base

from urllib.parse  import quote

from sqlalchemy.orm import sessionmaker # the things that we help us work with our db,
                                        #and connect us to our table

from sqlalchemy import MetaData

MetaData().create_all(bind= engine) 


#---->>Base.MetaData.create_all(engine) take how the db are made , create regarding the 
                                  #structure our my db 

#Session = sesssionmaker (binds = engine) copie all like a class

pw = 'ocGB@QkcA8'
host = 'python.hostingstudenti.fortechance.com'
user = 'c73db'
port = 3309
dialect = 'mysql'
schema = 'schema'

base = declarative_base() #because we have to recognise this the definition of line #3

#create_engine(from sqlalchemy import create_engine

#engine = create_engine('mysql://c73db:ocGB@QkcA8@host')

#engine = create_engine(f'mysql://c73db:{pwe}ocGB@QkcA8@host/schema')

#engine = create_engine(f'mysql://c73db:ocGB@QkcA8@{host}')

#engine = create_engine('from sqlalchemy import create_engine')

#engine = create_engine('mysql://c73db:ocGB@QkcA8@host')

engine = create_engine('mysql://c73db:ocGB@QkcA8@host/schema')

#conn = f'dialect://{c73db}:{ocGB@QkcA8}@{python.hostingstudenti.fortechance.com}/{schema}'

conn = f'{dialect}://{user}:{pw}@{host}/{schema}'

engine = create_engine(conn)



