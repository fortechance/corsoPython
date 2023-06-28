import PySimpleGUI as ps
from myTables import *
from myEngine import engine
from sqlalchemy import Select
from myNewPortfolio import doNewPortfolio, doNewWallet, doNewMouvement
from mySintesi import Sintesi
from myRefresh import *
import datetime



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

    selected_key = ''
    wallet_key = ''

    while True:

        event, values = windows.read()

        if event == ps.WIN_CLOSED or event == 'Exit':
            break
        elif event == '-refreshP-':
            if len(values['-refreshP-'])>0:
                selected_key = values['-refreshP-'][0][:3] 
                #ps.popup(f'Slezionata chiave, {selected_key}')

                porfolio_key = selected_key
                wallets = RefreshWallet(porfolio_key)

                windows['-refreshW-'].Update(wallets)
                windows['-refreshM-'].Update([])

        elif event == '-refreshW-':

            selected_key = values['-refreshW-'][0][:2]
            wallet_key = selected_key

            mouvements = RefreshMouvements(wallet_key)
            windows['-refreshM-'].Update(mouvements)


        elif event == 'Nuovo Portfolio':
            doNewPortfolio(cutente)

            valori = RefreshPorfolio(cutente)
            windows['-refreshP-'].Update(valori)
            windows['-refreshW-'].Update([])
            windows['-refreshM-'].Update([])
            #break
        elif event == 'Nuovo Wallet':

            nPortfolio = selected_key #values['-refreshP-'][0][:3] 
            if nPortfolio == '':
                continue
            else:
                doNewWallet(nPortfolio)
                wallets = RefreshWallet(nPortfolio) 
                windows['-refreshW-'].Update(wallets)
        elif event == 'Nuovo Movimento':
            doNewMouvement(wallet_key)
            
            mouvements = RefreshMouvements(wallet_key)
            windows['-refreshM-'].Update(mouvements)
            
        elif event == 'Sintesi':

            Sintesi(wallet_key)




            #break



    windows.close()
    pass


