from myEngine import engine
from sqlalchemy import text, insert, select
from myTables import user, causale, movimento
import datetime

with engine.connect() as cn:
    
    try:

        i =  insert(causale).values(
        codice = '123cis',
        descrizione = 'Incasso',
        segno = '+'
        )

        res = cn.execute(i)
        cn.commit()
        print('causale inserita')

        #cn.execute(text('insert into causali (codice, descrizione, segno) values ("newca","nuova causale", "+")'))

    except:
        cn.rollback()
        print('causale rifiutata')
    
    s=select(causale)
    res = cn.execute(s).all()
    for r in res:
        print(r)

    m=insert(movimento).values(
        importo = 100.45,
        dtMovimento = datetime.datetime.now(),
        codcausale = '123ci'
    )

    cn.execute(m)
    cn.commit()

    
    qq = select(causale)
    ret = cn.execute(qq).all()

    for r in ret:    
        print(r)
