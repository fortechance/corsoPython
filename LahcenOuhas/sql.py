from sqlalchemy import create_engine


engine= create_engine('mysql://c73db:ocGB@QkcA8@hostingstudenti.fortechance.com/schema')

from urllib.parse import quote
pw='ocGB@QkcA8'

pwe=quote(pw,safe="")

engine=create_engine(f'mysql://vc73db:{pwe}@hostingstudenti.fortechance.com/schema)')