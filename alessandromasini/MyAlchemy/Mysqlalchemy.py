from urllib.parse import quote
from sqlalchemy import create_engine, ForeignKey ,Table, Column,CHAR, Float, DateTime , Integer, String , MetaData

from sqlalchemy.orm import declarative_base, sessionmaker

#from sqlalchemy.ext.declarative import declarative_base
import datetime

user = 'c73db'
password = 'ocGB@QkcA8'
dialect = 'mysql'
host = 'python.hostingstudenti.fortechance.com'
schema = 'c73db'
#schema = 'mydb'
pwe = quote(password,safe='')
conn = f'{dialect}://{user}:{pwe}@{host}/{schema}'
engine = create_engine(conn, echo = True)
Base = declarative_base()

mdo = MetaData()

#definire le classi python che poi andranno nel database

#causali:

causali = Table(
    'causali',
    mdo,
    Column('CodCausale', String(5), primary_key = True),
    Column('Descrizione',String(50)),
    Column('Segno)', CHAR)
    )

mdo.create_all(engine)

Session = sessionmaker(engine)
session = Session()

causali.insert().values(CodCausale='12345', Descrizione = 'desc', Segno = '+')
Session.bind_mapper(mapper = mdo, bind=engine)
session.commit()

#session.add(cc)


c1=causali('12345','prova','+')

session.add(c1)
session.commit()

ret = session.query("causali").all()

for r in ret:
    print(r)











'''
engine = create_engine('mysql://c73db:ocGB@QkcA8@python.hostingstudenti.fortechance.com/c73db')
'''





