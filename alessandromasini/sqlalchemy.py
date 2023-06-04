
from urllib.parse import quote
from sqlalchemy import create_engine

pw = 'ocGB@QkcA8'
pwe = quote(pw,safe='')
engine = create_engine(f'mysql://c73db:{pwe}@python.hostingstudenti.fortechance.com/c73db')




'''
engine = create_engine('mysql://c73db:ocGB@QkcA8@python.hostingstudenti.fortechance.com/c73db')
'''





