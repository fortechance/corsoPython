from sqlalchemy import create_engine
from urllib.parse import quote
from sqlalchemy import Table, Column, Integer, String, MetaData, select
from sqlalchemy.ext.declarative import declarative_base


# //////////////////////////////////////////////////

# 89.40.173.164 - [192.168.10.16]
# python.hostingstudenti.fortechance.com
# schema:c73db
# user:c73db
# password:ocGB@QkcA8

# //////////////////////////////////////////////////

pw = "ocGB@QkcA8"
pwe = quote(pw, safe="")
# host = "89.40.173.164"
# host = "192.168.10.16"
host = "python.hostingstudenti.fortechance.com"
sch = "c73db"
us = "c73db"
dia = "mysql"

# --------------------------------------------------------
conn = f"{dia}://{us}:{pwe}@{host}/{sch}"
# --------------------------------------------------------

try:
    # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
    engine = create_engine(conn)
    print(
        f"Connection to the {host} for user {us} created successfully.")

    m = MetaData()

# ---------------------------------------------------------

    #  m.reflect(engine)
    #  for table in m.tables.values():
    #      print(table.name)
    #      for row in table.c :
    #          print(f"{column.name}-{column.type}")
    #         print("--------------------------")
    #         for column in table.c:
    #             print(f"{column.name}-{column.type}")
    #        print("--------------------------")
    #


# -----------------------------------------------


# ---------------------------------------------------------

    # students = Table(
    # 'students', m,
    # Column('id', Integer, primary_key = True),
    # Column('name', String(25)),
    # Column('lastname', String(25)),
    # )
    # m.create_all(engine)
# ---------------------------------------------------------

    t = Table("causali", m)
    stmt = select(t)
    print(stmt)
    t.drop(engine)


except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)
