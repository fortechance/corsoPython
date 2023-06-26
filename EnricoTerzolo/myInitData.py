from myEngine import engine
from sqlalchemy import TEXT, Insert, Select
from myTables import user, causale, movimento,tipowallet, portfolio,wallet
import datetime
import os

#intanto devo capire quale path devo utilizzare

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)

#prendere dai  csv i dti di base e inserirli nel DB

#users

#leggo il file csv
with engine.connect() as cn:

    file = BASE_DIR + '\\0_utenti.csv'
    with open(file, 'r') as fr:
        buffer = fr.read()
        righe=buffer.split('\n')

        riga = 0
        for r in righe:
            if riga == 0:
                riga +=1
                continue

            campi = r.split(';')

            codice = campi[0]
            nome = campi[1]
            cognome = campi[2]
            email = campi[3]
            password = campi[4]

            
            iuser = Insert(user).values(
                COD_UTENTE = codice,
                NOME = nome,
                COGNOME = cognome,
                EMAIL = email,
                PASSWORD = password
            )

            try:
                cn.execute(iuser)
                cn.commit()
            except Exception as e:
                cn.rollback()
                print(e.__str__)

    file = BASE_DIR + '\\0_causali.csv'
    with open(file, 'r') as fr:
        buffer = fr.read()
        righe=buffer.split('\n')

        riga = 0
        for r in righe:
            if riga == 0:
                riga +=1
                continue

            campi = r.split(';')

            codice = campi[0]
            descrizione = campi[1]
            segno = campi[2]
                    
            icaus = Insert(causale).values(
                CODICE = codice,
                DESCRIZIONE = descrizione,
                SEGNO = segno,
            )

            try:
                cn.execute(icaus)
                cn.commit()
            except Exception as e:
                cn.rollback()
                print(e.__str__)

    file = BASE_DIR + '\\0_tipowallet.csv'
    with open(file, 'r') as fr:
        buffer = fr.read()
        righe=buffer.split('\n')

        riga = 0
        for r in righe:
            if riga == 0:
                riga +=1
                continue

            campi = r.split(';')

            codice = campi[0]
            descrizione = campi[1]
            tipo = campi[2]
                    
            itw = Insert(tipowallet).values(
                CODICE = codice,
                DESCRIZIONE = descrizione,
                TIPO = tipo,
            )

            try:
                cn.execute(itw)
                cn.commit()
            except Exception as e:
                cn.rollback()
                print(e.__str__)

    #Ora nei cmpi ho i dati

    pass


#tipo Wallet

#causali
'''
with engine.connect() as cn:
    qu = insert(user).values()
'''




