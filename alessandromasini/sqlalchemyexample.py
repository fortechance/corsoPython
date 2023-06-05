

from sqlalchemy import create_engine

from urllib.parse import quote

pw = "ocGB@QkcA8"
pwe = quote(pw, safe ="")
engine = create_engine(f"mysql://c73db:{pwe}@python.hostingstudenti.fortechance.com/c73db")







