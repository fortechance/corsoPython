
from urllib.parse import quote
from sqlalchemy import create_engine, Column, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


user = 'c73db'
password = 'ocGB@QkcA8'
dialect = 'mysql'
host = 'python.hostingstudenti.fortechance.com'
schema = 'c73db'
pwe = quote(password,safe='')
conn = f'{dialect}://{user}:{pwe}@{host}/{schema}'
print(conn)

#engine = create_engine(f'mysql://c73db:{pwe}@python.hostingstudenti.fortechance.com/c73db')
engine = create_engine(conn)

Base = declarative_base()

class prova(Base):
    __tablename__ = 'prova'
    cod = Column(Integer, primary_key=True, autoincrement= 'auto') 
MetaData().create_all(bind=engine)




#MetaData.create_all(bind=engine)




'''
engine = create_engine('mysql://c73db:ocGB@QkcA8@python.hostingstudenti.fortechance.com/c73db')
'''





