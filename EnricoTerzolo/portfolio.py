from classiWallet import *
import PySimpleGUI as ps

def showPortfolio(p:portfolio):

    #se il PortFolio non ha wallet, occorre chiedere di ipostarne 1
    #se non ci sono movimenti occorre
    #indicarne uno, almeno di tipo fittizio
    #tipo il saldo 
    
    layout = [
        [ps.Text(f'Benvenuto {p.utente.nome}')],
        [ps.Text('I tuoi Wallet:'), ps.Text('I Tuoi movimenti')],
        [ps.Listbox(['w1','w2','w3']), ps.Listbox(['m1','m2','m3'])],
        [ps.Button('Aggiungi Wallet'), ps.Button('Aggiungi Movimento')],
        [ps.Text('Totale Spese'), ps.Text(''),ps.Text('Totale Entrate'), ps.Text('')],
        [ps.Button('Esci')]
    ]

    window = ps.Window('Portfolio',layout)

    while True:

        event, values = window.read()

        if event == ps.WIN_CLOSED:
            break    
    
    window.Close()
