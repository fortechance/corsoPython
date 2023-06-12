import PySimpleGUI as ps 
from classiWallet import *

def crea_wallet(w:wallet):

    ps.theme('DarkAmber')

    layout = [
        [ps.Text('Tipo Wallet'), ps.Listbox([], size = (None,5))],
        [ps.Text('Codice'), ps.Listbox([], size = (None,5))],
        [ps.Text('Descrizione'), ps.Listbox([], size = (None,5))],
        [ps.Button('OK'),ps.Button('Annulla')]
    ]