import PySimpleGUI as ps
from myTables import *
from myEngine import engine
from sqlalchemy import Select
from myNewPortfolio import doNewPortfolio

def RefreshMouvements(idWallet):

    with engine.connect() as cn:

        s = Select(movimento).where(movimento.c.IDWALLET == idWallet)
        listamovimenti = cn.execute(s).all()
        
        movlist = []
        for m in listamovimenti:
            movlist.append(f'{m[0]} - [{m[3]}] - € {m[1]} - {m[4]}')


    return movlist

def RefreshWallet(idportfolio):

    with engine.connect() as cn:

        s = Select(wallet).where(wallet.c.IDPORTFOLIO == idportfolio)
        walletlist = cn.execute(s).all()

        wallets = []
        for w in walletlist:
            wallets.append(f'{w[0]} - {w[1]}')

    return wallets


def RefreshPorfolio(cut):

    with engine.connect() as cn:

        s = Select(portfolio).where(portfolio.c.OWNER == cut)
        portlist = cn.execute(s).all()
        
        valori = []

        for p in portlist:

            valori.append(f'{p[0]} - {p[1]}')
           
        return  valori

def doDashboard( user, passw,cutente):

    
    ps.theme('green')

    valori = RefreshPorfolio(cutente)

    col1= [
        [ps.Text(f'I Tuoi Portfolio:')],
        [ps.Listbox((valori), size=(40,15), key='-refreshP-', enable_events=True, select_mode= 'listbox')]
    ]
    
    col2= [
        [ps.Text(f'I Tuoi Wallet:')],
        [ps.Listbox([], size=(40,15),key='-refreshW-', enable_events=True, select_mode = 'listbox')]
    ]
    col3= [
        [ps.Text(f'I Tuoi Movimenti:')],
        [ps.Listbox([], size=(80,15),key = '-refreshM-', enable_events = True, select_mode = 'listbox')]
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
            selected_key = values['-refreshP-'][0][:3] 
            #ps.popup(f'Slezionata chiave, {selected_key}')

            porfolio_key = selected_key
            wallets = RefreshWallet(porfolio_key)

            windows['-refreshW-'].Update(wallets)

        elif event == '-refreshW-':

            selected_key = values['-refreshW-'][0][:2]
            wallet_key = selected_key

            mouvements = RefreshMouvements(wallet_key)
            windows['-refreshM-'].Update(mouvements)


        elif event == 'Nuovo Portfolio':
            doNewPortfolio(cutente)

            chiavi = []
            valori = []
            chiavi, valori , combined = RefreshPorfolio(cutente)
            windows['-refreshP-'].Update(values = (combined))
            #break
        elif event == 'Nuovo Wallet':
            break
        elif event == 'Nuovo Movimento':
            break

    windows.close()
    pass


