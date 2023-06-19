from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData

from sqlalchemy.ext.declarative  import declarative_base   # vado a dichiarare cosa c'è sulla roba esterna e prendo la versione base della tabella

from sqlalchemy.orm import sessionmaker             # cosa che mi permette di lavorare con le mie classi come se lavorassi sulla tabelladel databese (connetto le tabelle alle mie classi e le mie classi alle tabelle)

# from urllib.parse import quote

# pw='c73db:ocGB@QkcA8'
# pwe = quote(pw,safe='')   #password encoded - forse non serve farlo

# engine = create_engine(f'mysql://c73db:{pwe}@python.hostingstudenti.fortechance.com/c73db') 

# engine è la prima variabile globale che mi serve

                                                    # memorizzo le variabili per la connessione
dialect = 'mysql'
user = 'c73db'
password = 'ocGB@QkcA'
host = 'python.hostingstudenti.fortechance.com'
schema = 'c73db'                                    # normalmente non è uguale allo username


conn = f'{dialect}://{user}:{password}@{host}/{schema}'  # mi connetto al database

engine = create_engine (conn)           # motore che parla il dialetto che vogliamo noi, con lo schema che vgliamo e i dati di connessione che abbiamo

Base = declarative_base()

class Causale (Base):                                      # classe causale - stiamo dicendo cosa vogliamo che esista nel database
    __tablename__ = 'causali'                             # nome tabella causali
    codCausale = Column(String(5),primary_key=True)      # colonna tipo stringa lunga 5 caratteri, che è chiave primaria
    descCausale = Column(String(50))
    segnoCausale = Column(String(1))

# sessione: oggetto che mi permette di scrivere i dati e consolidarli

MetaData().create_all(bind=engine)                 # della classe Metadata prendi come sono fatte le cose e crea la struttura sul disco fisso e mettila sull'engine
                                            # collegamento ponte tra le tabelle e le classi

Session = sessionmaker(bind=engine)         # prende l'engine e lo trasforma nelle mie classi

session = Session()


# definisco classi che rispecchino i contenuti delle cose che mi servono
# devo derivare da una classe base una tabella e descrivere quelle colonne (ogni colonnaha il suo tipo)

