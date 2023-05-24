from classiWallet import *
import PySimpleGUI as ps
from ScriptPaola_01 import initTipoWallet as Tw

def addWallet(tw):

    #se il PortFolio non ha wallet, occorre chiedere di ipostarne 1
    #se non ci sono movimenti occorre
    #indicarne uno, almeno di tipo fittizio
    #tipo il saldo
    
     
    
    layout = [
        [ps.Text('Tipo Wallet'), ps.Combo(tw)],
        [ps.Text('Codice Wallet'), ps.Input(key = '-CODICEW-')],
        [ps.Text('Descrizione Wallet'), ps.Input(key = '-DESCW-')],
        [ps.Button('Aggiungi Wallet'), ps.Button('Annulla')],
    ]

    window = ps.Window('Wallet',layout, size = (300,300))

    while True:

        event, values = window.read()

        if event == ps.WIN_CLOSED:
            break
        elif event == 'Annulla':
            showPortfolio()
        
    window.Close()

def showPortfolio(p:portfolio):

    #se il PortFolio non ha wallet, occorre chiedere di ipostarne 1
    #se non ci sono movimenti occorre
    #indicarne uno, almeno di tipo fittizio
    #tipo il saldo
    
    wl = []
    for w in p.wallets:
        wl.append(w)
    
    layout = [
        [ps.Text(f'Benvenuto {p.utente.nome}')],
        [ps.Text('I tuoi Wallet:'), ps.Text('I Tuoi movimenti')],
        [ps.Listbox(wl), ps.Listbox(['m1','m2','m3'])],
        [ps.Button('Aggiungi Wallet'), ps.Button('Aggiungi Movimento')],
        [ps.Text('Totale Spese'), ps.Text(''),ps.Text('Totale Entrate'), ps.Text('')],
        [ps.Button('Esci')]
    ]

    window = ps.Window('Portfolio',layout)

    while True:

        event, values = window.read()

        if event == ps.WIN_CLOSED or event == 'Esci':
            break
        elif event == 'Aggiungi Wallet':
            tw = Tw('0_tipowallet.csv')
            addWallet(tw)
    
    window.Close()
