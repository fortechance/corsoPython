
from sqlalchemy_my_engine import engine
from sqlalchemy import table, column, Integer, String, CHAR, MetaData

metaobj = MetaData()

user = table(
    "users",
    metaobj,
    column("ID", Integer, primarykey=True),
    column("Nome", String(25)),
    column("Cognome", String(25)),
    column("username", String(25)),
    column("password", String(25)),
    )

causale = table(
    "causali",
    metaobj,
    column("ID", Integer, primarykey=True),
    column("Descrizione", String(25)),
    column("Segno", CHAR(25)),
    )