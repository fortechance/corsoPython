from myEngine import engine
from sqlalchemy import text, insert, select
from myTables import user, causale, movimento
import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)

#estraggo gli user dal csv per inserirli nel db
userCSV = BASE_DIR + '\\csv\\utenti.csv'


with engine.connect() as cn:
    with open(userCSV, 'r') as fr:
        buffer = fr.read()
        righe = buffer.split('\n')
        nriga = 0
        
        for riga in righe:
            if (nriga == 0):
                nriga +=1
                continue

            colonne = riga.split(';')
            #ora bbiamo le colonne suddivise riga per riga

            codU = colonne[0]
            nomeU = colonne[1]
            cognomeU = colonne[2]
            emailU = colonne[3]
            passU = colonne[4]
    
            i =  insert(user).values(
            COD_UTENTE = codU,
            NOME = nomeU,
            COGNOME = cognomeU,
            EMAIL = emailU,
            PASSWORD = passU
            )
            
            try:
                cn.execute(i)
                cn.commit()
                print('Utente inserito')
            except Exception as e:
                cn.rollback()
                print(e.__str__)
                
                
    '''
    
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
    
    '''
