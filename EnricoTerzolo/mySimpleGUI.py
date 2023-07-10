# import PySimpleGUI
from myTables import * 
from myEngine import engine
from login_paola import doLogin
from myDashboard import doDashboard
from json import dumps
import requests

from sqlalchemy import Select

# devo fare un login, poi il resto è di sonseguenza
a=True

while a:

    username, password = doLogin()

    reqdata = {}
    reqdata['USER'] = username
    reqdata['PASSWORD'] = password

    ret = requests.post('http://127.0.0.1/main/login',data = dumps(reqdata))

    risposta = ret.json



    #dobbiamo chiamare la API che f il login


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

