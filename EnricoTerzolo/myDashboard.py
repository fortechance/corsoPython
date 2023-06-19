import PySimpleGUI as ps
from myTables import *
from myEngine import engine
from sqlalchemy import Select

def doDashboard( user, passw,cutente):

    with engine.connect() as cn:

        s = Select(portfolio).where(portfolio.c.OWNER == cutente)
        portlist = cn.execute(s).all()

    ps.theme('green')

    col1= [
        [ps.Text(f'I Tuoi Portfolio:')],
        [ps.Listbox(portlist, size=(40,15))]
    ]
    
    col2= [
        [ps.Text(f'I Tuoi Wallet:')],
        [ps.Listbox([], size=(40,15))]
    ]
    layout = [
        [ps.Text(f'Benvenuto {user}')],
        [ps.Column(col1),ps.VerticalSeparator(), ps.Column(col2)],
        [ps.HorizontalSeparator()],
        [ps.Button('Nuovo Portfolio',key='-newporfolio-'),
         ps.Button('Nuovo Wallet',key='-newwallet-'),
         ps.Button('Nuovo Movimento',key='-newmovimento-'),
         ps.Button('Sintesi', pad=(100,0))       
         ]               
    ]

    windows = ps.Window('Dashboard',layout, size=(800,600))

    while True:

        event, values = windows.read()

        if event == ps.WIN_CLOSED or event == 'Exit':
            break


    windows.close()
    pass


