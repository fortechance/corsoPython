#CLASSI PER INTEROGARE IL BACKEND

from flask import request
from flask import json
from flask import jsonify
import requests


class ApiBase:

    def __init__(self, urlBase, UUIDBase):

        self.urlBase = urlBase
        self.UUIDBase = UUIDBase

class cLogin(ApiBase):

    def __init__(self, url, rotta, user, password,uuidbase, metodo):

        super().__init__( url, uuidbase )
        self.user = user
        self.password = password
        self.rotta = rotta
        
   
    def CallLogin(self):

        myURI = self.urlBase + '/' + self.rotta
        myData = {}
        myData['USER'] = self.user
        myData['PASSWORD'] = self.password

        risposta = requests.post(myURI, json = json.dumps(myData))
        # risposta = request.post(myURI, json=json.dumps(myData))

        if risposta.status_code == 200:

            data = risposta.json
            self.newuuid = data['UUID']

            self.loginOK = 'OK'

        else:
            
            self.loginOK = 'KO'

