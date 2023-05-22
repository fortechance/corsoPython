# questo file contiene tutto chò che serve per il login

import PySimpleGUI as ps 

def doLogin():

    ps.theme('DarkAmber')

    layout = [
        [ps.Text('Inserire dati di Login')],
        [ps.Text('Username: '), ps.InputText(key = '-user-')],
        [ps.Text('Password: '), ps.InputText(key = '-pass-', password_char = '*')],
        [ps.Button('Login'),ps.Button('Exit')]
    ]

    windows = ps.Window('login',layout)

    while True:

        event, values = windows.read()

        if event == ps.WIN_CLOSED or event == 'Exit':
            user = None
            passw = None
            break

        elif event == 'Login':
            user = (values['-user-'])
            passw = (values['-pass-'])
            break

    return user, passw    

    