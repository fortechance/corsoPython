from sqlalchemy import create_engine
from urllib.parse import quote

user = 'c73db'
password = 'ocGB@QkcA8'
dialect = 'mysql'
host = 'python.hostingstudenti.fortechance.com'
schema = 'c73db'
#forzo la password come stringa perchè c'è una @ che crea disordine con la connessione
pwe = quote(password,safe='')
conn = f'{dialect}://{user}:{pwe}@{host}/{schema}'

print("Creazione dell'engine di database:")
print(conn)

#engine = create_engine(conn, echo=True)
engine = create_engine(conn)
