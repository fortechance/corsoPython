
import PySimpleGUI
from myTables import *
from myEngine import engine
from login_paola import doLogin
from sqlalchemy import Select

# devo fare un login, poi tutto il resto

username, password = doLogin()

slogin = Select(user).where(user.c.NOME == username and user.c.PASSWORD == password )
with engine.connect as cn:
    try:
        results = cn.execute(slogin).one()
        login = True
        print("login eseguito")
    except:
        login = False
        print("login fallito")
    else:
        pass
    