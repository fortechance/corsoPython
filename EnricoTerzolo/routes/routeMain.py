from flask import Blueprint,  request, jsonify
from myEngine import engine
from myTables import *
from myRefresh import * 
from sqlalchemy import Select
from uuid import uuid4
import json 
from flask import jsonify

from loginAttivi import LoginAttivi

main_bp = Blueprint('main',__name__)

@main_bp.route('/', methods = ['GET'])
def Index():
    return 'Pagina di index, ti invito a effettuare il Login su http://127.0.0.1/login'

@main_bp.route('/login', methods = ['POST'])
def login():
    
    rlogin = request
    dati = rlogin.json
    print(dati)

    dt = json.loads(dati)

    nome = dt['USER']
    pasw = dt['PASSWORD']

    slogin = Select(user).where (user.c.NOME == nome).where(user.c.PASSWORD == pasw)
    
    #slogin = Select(user)
   
    with engine.connect() as cn:
        try:
            results = cn.execute(slogin).one()
            if (results):
                codutente = results.COD_UTENTE
                print('login eseguito')
                reterr = ''
            else:
                codutente = ''
                reterr = 'not found'

        except Exception as e:

            codutente = ''
            print('Login Fallito')
            reterr = 'fallimento'

    loginOK = {}
    if reterr == '':
        #creo un codice univoco
        unicod = str(uuid4())
    else:
        unicod = ''

    loginOK ['CODICE'] = codutente
    loginOK ['USERNAME'] = nome
    loginOK ['PASSWORD'] = pasw
    loginOK ['UUID'] = unicod

    LoginAttivi[unicod] = loginOK

    print (LoginAttivi)

    if unicod == '':
        #return json.dumps(loginOK), 404         
        return jsonify(loginOK),404
    else:
        #return json.dumps(loginOK), 200
        return jsonify(loginOK), 200
@main_bp.route('/dashboard', methods = ['POST'])
def showDashboard():
    
    rdas = request
    dati = rdas.json

    uuid = dati['UUID']
    if uuid in LoginAttivi.keys():
        utente = LoginAttivi[uuid]['CODICE']
    else:
        utente = 'SCONOSCIUTO' 
    db = {}
    db['portfolios'] = {}

    if uuid in LoginAttivi.keys():
        print ('Dashboard allowed')
        unicod = str(uuid4())
        vecchio = LoginAttivi[uuid]
        LoginAttivi[unicod] = vecchio
        foo = LoginAttivi.pop(uuid)

        # la return di un dizionario (quindi oggetto json) con ad esempio la lista dei portfolio di quell'utente

        newPortfolios = RefreshPorfolio(utente, True)
        ret = {}
        ret['UUID'] = unicod
        ret['PORTFOLIOS'] = newPortfolios

        return jsonify(ret), 200

    else:
        ret = {}
        ret['UUID'] = ''
        ret['PORTFOLIOS'] = {}

        return jsonify(ret), 404

 