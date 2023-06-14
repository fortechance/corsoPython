from myTables import metaobj, user, causale
from myEngine import engine



metaobj.create_all(bind = engine)

