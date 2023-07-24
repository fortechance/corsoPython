import PySimpleGUI as sg
sg.set_options(font=('Arial Bold', 16))
# Definisce il layout della finestra
layout = [[sg.Text('Cod. causale      :'), sg.Input(size=(2, 1), key='-CAUSALE-'),
           sg.Text(''), sg.Input(size=(40, 1), key='-DESCRIZIONE-'), sg.FileBrowse()],
          [sg.Text('Cod. causale 2   :'), sg.Input(size=(2, 1), key='-CAUSALE2-'),
           sg.Text(''), sg.Input(size=(40, 1), background_color='Yellow'), sg.FileBrowse()],
          [sg.Text('Tipo movimento  :'), sg.Input(size=(1, 1), key='-TIPO-'), sg.Text('    E=Entrata U=Uscita A=Altro '), ],
          [sg.Button('Inserisci', button_color=('white', '#FF8DC7')),
           sg.Button('Variazione',button_color=('white', '#FFACC7') ),
           sg.Button('Cancella', button_color=('white', 'orange')),
           sg.Button('Stampa', button_color=('white', '#FFC6C2') ),
           sg.Button('Esporta-csv', button_color=('white' , '#AEE2FF') ),
           sg.Button('Conferma', button_color=('white', '#62A8D1') ),
           sg.Button('Uscita', button_color=('white' , '#93C6E7')) ]]

# Crea la finestra
window = sg.Window('Causali di movimentazione', layout)
# Loop principale per gestire gli eventi
while True:
    event, values = window.read()
    # Controllo degli eventi
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Conferma':
        input1_value = values['-CAUSALE-']
        input2_value = values['-DESCRIZIONE-']
        input3_value = values['-CAUSALE2-']
        input4_value = values['-TIPO-']
        sg.popup(f'Inseriti : Cod. causale: {input1_value}, Descrizione: {input2_value}, Cod. causale2 {input3_value}, Tipo movimento {input4_value}')
# Chiude la finestra
window.close()
