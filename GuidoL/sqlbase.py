from sqlalchemy import create_engine
from urllib.parse import quote

pw = "ocGB@QkcA8"
pwe = quote(pw, safe="")

# 89.40.173.164 - [192.168.10.16]
host = "python.hostingstudenti.fortechance.com"
sch = "c73db"
us = "c73db"
# password:ocGB@QkcA8

engine = create_engine(f"mysql://{us}:{pwe}@{host}/{sch}")

# engine = create_engine("mysql+mysqldb://scott:tiger@localhost/test")


# 89.40.173.164 - [192.168.10.16]
# python.hostingstudenti.fortechance.com
# schema:c73db
# user:c73db
# password:ocGB@QkcA8
