# import PySimpleGUI
from myTables import * 
from myEngine import engine
from login_paola import doLogin
from myDashboard import doDashboard
import json
import requests

from sqlalchemy import Select

# devo fare un login, poi il resto è di sonseguenza

while True:

    username, password = doLogin()

    reqdata = {}
    reqdata['USER'] = username
    reqdata['PASSWORD'] = password

    ret = requests.post('http://127.0.0.1/main/login',json = json.dumps(reqdata))

    risposta = ret.json
    ris = json.loads(risposta)
    


if a== False:
    username = 'p'
    password = 'a'
    codutente = '007'

#print(username + ' '+password )    

doDashboard(username, password, codutente)

