from create_engine import engine
from sqlalchemy import text
from mytables import user

#paradigma 2
user.insert().values(nome = "pippo", cognome = "paperino")
user.insert().values(nome = "enrico", cognome = "terzolo", username = "prova", password = "nonteladico")

with engine.connect() as cn:
    res = cn.execute(text("select * from users")).all()

'''
paradigma 1
with engine.connect() as cn:
    res = cn.execute(text("insert into users values("a","b","c","d")")).all()
    cn.commit()

with engine.connect() as cn:
    res = cn.execute(text("select * from users")).all()

print(res)

'''
