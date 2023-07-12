import PySimpleGUI as ps
from myTables import *
from myEngine import engine
from sqlalchemy import Select
from myNewPortfolio import doNewPortfolio, doNewWallet, doNewMouvement
from mySintesi import Sintesi
from myRefresh import *
import datetime
import requests
from flask import json

#def doDashboard( user, passw,cutente):
def doDashboard(uuid):

    #formuliamo la richiesta:

    reqdata = {}
    reqdata['UUID'] = uuid

    #eseguiamo la request
    ret = requests.post('http://127.0.0.1/main/dashboard',json = json.dumps(reqdata))
    if ret.status_code == 200:
        risposta = ret.json()
    else:
        risposta = 'Errore: ' + str(ret.status_code)


    print(risposta)
    return

    ps.theme('green')

    valoriq = RefreshPorfolio(cutente, True)

    listap = []
    for q in valoriq:

        chiave = q
        descr = valoriq[q]['DESCRIZIONE']
        owner = valoriq[q]['OWNER']

        elemento = f'{chiave} - {descr}'

        listap.append(elemento)

    col1= [
        [ps.Text(f'I Tuoi Portfolio:')],
        [ps.Listbox((listap), size=(40,15), key='-refreshP-', enable_events=True, select_mode= 'listbox')]
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
         ps.Button('Sintesi', pad=(100,0))],
         [ps.Listbox([], size = (140,15), key = '-sintesi-', enable_events = True)]       
                      
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

            try:
                selected_key = values['-refreshW-'][0][:2]
                wallet_key = selected_key

                mouvements = RefreshMouvements(wallet_key)
                windows['-refreshM-'].Update(mouvements)
            except:
                continue

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

            listasintesi = Sintesi(wallet_key)
            windows['-sintesi-'].Update(listasintesi)



            #break



    windows.close()
    pass


