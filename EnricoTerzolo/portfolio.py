from classiWallet import *
import PySimpleGUI as ps

def addWallet(wtype):

    #creaare una nuova finestra con un nuovo layou
    wt = []
    for wq in wtype:
        wt.append(wq)

    layout = [
        [ps.Text('Tipo Wallet: '), ps.Combo(wt, key = '-TIPOW-')],
        [ps.Text('Codice: '), ps.Input(key = '-CODICEW-')],
        [ps.Text('Descrizione: '), ps.Input(key = '-DESCRW-')],
        [ps.Button('OK'), ps.Button('Annulla')]
    ]

    window = ps.Window('Aggiungi Wallet',layout,size = (300,300))
    
    while True:
        event, values = window.read()

        action = ''

        if event == ps.WIN_CLOSED:
            break
        
        if event == 'OK':

            w = None

            cw = values['-CODICEW-']
            ds = values['-DESCRW-']
            tw = values['-TIPOW-']

            w = wallet(tw,ds,cw)
            action = 'OK'
            break
    

    if action == 'OK':
        return w

    pass

def showPortfolio(p:portfolio, wtype):

    #se il PortFolio non ha wallet, occorre chiedere di ipostarne 1
    #se non ci sono movimenti occorre
    #indicarne uno, almeno di tipo fittizio
    #tipo il saldo 
    
    wl = []

    for w in p.wallets:
        wl.append(w)


    colonna1 = [
        [ps.Text('I Tuoi Wallet')],
        [ps.Listbox(wl, size = (None,5))],
        [ps.Text('Totale Entrate'), ps.Text('0.00',justification = 'right')]
    ]

    colonna2 = [
        [ps.Text('I Tuoi Movimenti0')],
        [ps.Listbox([], size = (None,5))],
        [ps.Text('Totale Spese'), ps.Text('2310.00' ,justification = 'right')]
    ]
    
    pulsanti = [
        [ps.Button('Esci'), 
         ps.Button('Aggiungi Wallet'), 
         ps.Button('Aggiungi Movimento')]
    ]
    layout = [
        [ps.Text(f'Benvenuto {p.utente.nome}')],
        [ps.Column(colonna1),ps.Column(colonna2)],
        [ps.HorizontalSeparator()],
        [ps.Column(pulsanti)]
    ]

    window = ps.Window('Portfolio',layout,size = (600,600))


    while True:

        event, values = window.read()

        if event == ps.WIN_CLOSED:
            break    

        if event == 'Aggiungi Wallet':
            wnew = addWallet(wtype)
            p.addWallet(wnew)

            #aggiorno la videata


    window.Close()
