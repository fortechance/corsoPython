import PySimpleGUI as psg

def AggiungiWallet():
    
    psg.theme('SandyBeach')

    layout = [
    [psg.Text('Tipo Wallet',justification='left'), 
    psg.Combo(['Risparmio','Mutuo','Vacanze', 'Conto Corrente'], default_value='Risparmio')],
    [psg.Text('Codice Wallet',justification='left'), 
    psg.Input('', enable_events=True, key='-INPUT-', expand_x=True, justification='left')],
    [psg.Text('Descrizione', justification='left'), 
    psg.Input('', enable_events=True, key='-INPUT-', expand_x=True, justification='left')],
    [psg.Button('Aggiungi', font=('Lucida',12)), psg.Button('Annulla')]
    ]

    win = psg.Window('Crea un nuovo wallet', layout)

    while True:

        event,values=win.read()

        if event == psg.WIN_CLOSED or event == 'Annulla':
            break
        elif event == 'Aggiungi':
            break

    win.Close()



