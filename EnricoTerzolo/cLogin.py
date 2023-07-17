#CLASSI PER INTEROGARE IL BACKEND

from flask import request
from flask import json
from flask import jsonify

class ApiBase:

    def __init__(self, urlBase, UUIDBase):

        self.urlBase = urlBase
        self.UUIDBase = UUIDBase

class cLogin(ApiBase):

    def __init__(self, url, rotta, user, password,uuidbase, metodo):

        super.__init__(self, url, uuidbase )
        self.user = user
        self.password = password
        self.rotta = rotta
        
   
    def CallLogin(self):

        myURI = super.urlBase + self.rotta
        myData = {}
        myData['USERNAME'] = self.user
        myData['PASSWORD'] = self.password

        risposta = request.post(myURI, json=json.dumps(myData))

        if risposta.status_code == 200:

            data = risposta.json
            self.newuuid = data['UUID']

            self.loginOK = 'OK'

        else:
            
            self.loginOK = 'KO'

