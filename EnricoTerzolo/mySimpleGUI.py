# import PySimpleGUI
from myTables import * 
from myEngine import engine
from login_paola import doLogin
from myDashboard import doDashboard
import json
#from flask import request
import requests

from sqlalchemy import Select

# devo fare un login, poi il resto è di sonseguenza

while True:

    username, password = doLogin()

    reqdata = {}
    reqdata['USER'] = username
    reqdata['PASSWORD'] = password

    ret = requests.post('http://127.0.0.1/main/login',json = json.dumps(reqdata))
    if ret.status_code == 200:
        risposta = ret.json()
        myuuid = risposta['UUID']
        break
    else:
        risposta = 'Errore: ' + str(ret.status_code)
        myuuid = ''
print(
    risposta['USERNAME'],
    risposta['PASSWORD'],
    risposta['CODICE']
    )

doDashboard(myuuid)

#doDashboard(
#    risposta['USERNAME'],
#    risposta['PASSWORD'],
#    risposta['CODICE']
#   )

