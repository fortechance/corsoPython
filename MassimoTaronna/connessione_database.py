from sqlalchemy import create_engine

from urllib.parse import quote

pw='c73db:ocGB@QkcA8'
pwe = quote(pw,safe='')   #password encoded - forse non serve farlo

engine = create_engine(f'mysql://c73db:{pwe}@python.hostingstudenti.fortechance.com/c73db')   

# engine è la prima variabile globale che mi serve