import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Inserisci di seguito i parametri di un nuovo Wallet:')],
            #[sg.Text('Inserisci TipoWallet')],
            #[sg.Combo('variabile1, variabile2, variabile3',key='tipowallet')],
            [sg.Text("Tipo Wallet",size=(10,1)),sg.Combo(["variabile1","variabile2","variabile3"],key='tipowallet',size=(40,1))],
            [sg.Text('Inserisci Codice'), sg.InputText()],
            #[sg.Listbox(values=['Welcome Drink', 'Extra Cushions', 'Organic Diet','Blanket', 'Neck Rest'], select_mode='extended', key='fac', size=(30, 6))],
            [sg.Text('Descrizione'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Annulla')] ]

# Create the Window
window = sg.Window('Wallet - Nuovo Wallet', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Annulla': # if user closes window or clicks cancel
        break
    print('Hai inserito ', values[0])

window.close()