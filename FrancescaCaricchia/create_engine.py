from sqlalchemy import create_engine
from urllib.parse import quote

user = 'c73db'
password = 'ocGB@QkcA8'
dialect = 'mysql'
host = 'python.hostingstudenti.fortechance.com'
schema = 'c73db'
pwe = quote(password,safe='')
conn = f'{dialect}://{user}:{pwe}@{host}/{schema}'

print("creazione dell'engine di database")

engine = create_engine(conn, echo = True) 
#echo mi fa vedere passo passo le istr di sql