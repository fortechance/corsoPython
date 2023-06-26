from myTables import metaobj
from myTables import user, causale, tipowallet, portfolio
from myTables import wallet, movimento
from myEngine import engine


metaobj.create_all(bind = engine)

