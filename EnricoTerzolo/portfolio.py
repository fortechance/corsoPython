from classiWallet import *
import PySimpleGUI as ps

def showPortfolio(p:portfolio):

    #se il PortFolio non ha wallet, occorre chiedere di ipostarne 1
    #se non ci sono movimenti occorre
    #indicarne uno, almeno di tipo fittizio
    #tipo il saldo 
    
    colonna1 = [
        [ps.Text('I Tuoi Wallet')],
        [ps.Listbox([], size = (None,5))],
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
    
    window.Close()
