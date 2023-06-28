# import PySimpleGUI
from myTables import *
from myEngine import engine
from login_paola import doLogin
from myDashboard import doDashboard

from sqlalchemy import Select

# devo fare un login, poi il resto è di sonseguenza
a=True

while a:

    username, password = doLogin()

    slogin = Select(user).where(user.c.NOME == username and user.c.PASSWORD == password)
    with engine.connect() as cn:
        try:
            results = cn.execute(slogin).one()
            login = True
            codutente = results.COD_UTENTE
            print('login eseguito')
            break

        except: 

            login = False
            print ('login fallito')
            username = ''
            password = ''
            codutente = ''
            continue    


    # dobbiamo portarci appresso chi ha fatto il login.

if a== False:
    username = 'p'
    password = 'a'
    codutente = '007'

#print(username + ' '+password )    

doDashboard(username, password, codutente)

