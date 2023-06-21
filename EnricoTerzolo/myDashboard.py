import PySimpleGUI as ps
from myTables import *
from myEngine import engine
from sqlalchemy import Select
from myNewPortfolio import doNewPortfolio


def RefreshPorfolio(cut):

    with engine.connect() as cn:

        s = Select(portfolio).where(portfolio.c.OWNER == cut)
        portlist = cn.execute(s).all()

        chiavi = []
        valori = []

        for p in portlist:

            chiavi.append(p[0])
            valori.append(f'{p[0]} - {p[1]}')

            
    return chiavi, valori

def doDashboard( user, passw,cutente):

    
    ps.theme('green')

    chiavi, valori = RefreshPorfolio(cutente)

    col1= [
        [ps.Text(f'I Tuoi Portfolio:')],
        [ps.Listbox((valori), size=(40,15), key='-refreshP-', enable_events=True)]
    ]
    
    col2= [
        [ps.Text(f'I Tuoi Wallet:')],
        [ps.Listbox([], size=(40,15))]
    ]
    col3= [
        [ps.Text(f'I Tuoi Movimenti:')],
        [ps.Listbox([], size=(40,15))]
    ]
    layout = [
        [ps.Text(f'Benvenuto {user}')],
        [ps.Column(col1),ps.VerticalSeparator(), ps.Column(col2),ps.VerticalSeparator(),ps.Column(col3)],
        [ps.HorizontalSeparator()],
        [ps.Button('Nuovo Portfolio'),
         ps.Button('Nuovo Wallet'),
         ps.Button('Nuovo Movimento'),
         ps.Button('Sintesi', pad=(100,0))       
         ]               
    ]

    windows = ps.Window('Dashboard',layout, finalize = True)
    windows.Maximize()

    while True:

        event, values = windows.read()

        if event == ps.WIN_CLOSED or event == 'Exit':
            break
        elif event == '-refreshP-':
            selezione = values['-refreshP-'][0]
            chiave = values['-refreshP-'][0][1]
            ps.popup(selezione, chiave)

        elif event == 'Nuovo Portfolio':
            doNewPortfolio(cutente)

            chiavi = []
            valori = []
            chiavi, valori = RefreshPorfolio(cutente)
            windows['-refreshP-'].Update(values = (valori))
            #break
        elif event == 'Nuovo Wallet':
            break
        elif event == 'Nuovo Movimento':
            break

    windows.close()
    pass


