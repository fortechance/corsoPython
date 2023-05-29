from classiWallet import *
import PySimpleGUI as ps
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

lista_wallet = {}

def initTipoWallet(fileName):

    file = BASE_DIR + '\\' + fileName
    #print(file)
    with open(file, 'r') as f:
        dati = f.read()

    righe = dati.split('\n')
    nriga = 0

    for riga in righe:
        if (nriga == 0):
            nriga += 1
            continue

        colonne = riga.split(';')
        # ora bbiamo le colonne suddivise riga per riga

        codice = colonne[0]
        descrizione = colonne[1]
        tipo = colonne[2]

        # lo aggiungo al dizionario

        w = {}
        w['Descrizione'] = descrizione
        w['Tipo'] = tipo

        lista_wallet[codice] = w


def select_wallet(dict):

    ps.theme('DarkAmber')

    walletti = []
    for d in dict:
        dd= dict[d].get("Descrizione")
        walletti.append(dd)
    print (walletti)    

    layout = [[ps.Text('select wallet')],
              [ps.Listbox(walletti, size=(15, len(walletti)), key='-WALLET-')],
              [ps.Text('Codice'), ps.InputText(key='-CODICE-')],
              [ps.Text('Descrizione'), ps.InputText(key='-DESCRIZIONE-')],
              [ps.Button('Ok')],]

    window = ps.Window('Walletssss', layout)

    while True:                  # the event loop
        event, values = window.read()
        if event == ps.WIN_CLOSED:
            break
        if event == 'Ok':
            if values['-WALLET-']:    # if something is highlighted in the list
                ps.popup(f"Your wallet {values['-WALLET-'][0]}")
    window.close()


   ###########################################
initTipoWallet("0_causale_taronna.csv")

select_wallet(lista_wallet)

pass
