## t-depositi.py
## data agg.  24/05/2023
import PySimpleGUI as sg
sg.set_options(font=('Arial Bold', 16))
# Definisce il layout della finestra
layout = [
        [sg.Button(image_filename="F:\img2023\lg2023.png", image_size=(70, 30), border_width=0, button_color=('white') ),sg.Text(' ' * 50), sg.Text("RILEVAZIONE GIACENZE MEDIANTE PARAMETRI")],
            [sg.HorizontalSeparator()],
           [sg.Text('Cod. azienda      :'), sg.Input(size=(5, 1), key='-AZIENDA-'),
           sg.Text(''), sg.Input(size=(60, 1), key='-DESCRIZIONE-'), sg.Text(' ' * 20), sg.FileBrowse()],
          [sg.Text('Cod. deposito    : '), sg.Input(size=(4, 1), key='-CODDEPOSITO-'),
           sg.Text('' * 2), sg.Text(''), sg.Input(size=(60, 1), key='-DESCRDEPOSITO-'), sg.Text(' ' * 20), sg.FileBrowse()],
          [sg.Text('Cod. prodotto     : '), sg.Input(size=(21, 1), key='-CODPRODOTTO-'),
          sg.Text(''), sg.Input(size=(55, 1), key='-DESCRPRODOTTO-'), sg.FileBrowse() ],
          [sg.Text('Data ult. entarta : '), sg.Input(size=(12, 1), key='-DATAENTRATA-')],
          [sg.Text('Data ult. uscita   : '), sg.Input(size=(12, 1), key='-DATAUSCITA-')],
          [sg.Text('Saldo iniziale     :  '), sg.Input(size=(60, 1), key='-SALDOINIZIALE-')]  ,
          [sg.Text('Disponibilità       :  '), sg.Input(size=(60, 1), key='-DISPONIBILITA-', background_color='Yellow')],

          ## [sg.Text('' * 60)],
          ## [sg.Text('-' * 180)],
          [sg.HorizontalSeparator()],
          [ sg.Text(' ' * 42),  sg.Button('Inserisci', button_color=('white', '#FF8DC7')),
           sg.Button('Variazione',button_color=('white', '#FFACC7') ),
           sg.Button('Cancella', button_color=('white', 'orange')),
           sg.Button('Stampa', button_color=('white', '#FFC6C2') ),
           sg.Button('Esporta-csv', button_color=('white' , '#AEE2FF') ),
           sg.Button('Conferma', button_color=('white', '#62A8D1') ),
           sg.Button('Uscita', button_color=('white' , '#93C6E7')) ]]

# Crea la finestra
window = sg.Window('Giacenze', layout)
# Loop principale per gestire gli eventi
while True:
    event, values = window.read()
    # Controllo degli eventi
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Conferma':
        input1_value = values['-AZIENDA-']
        input2_value = values['-DESCRIZIONE-']
        input3_value = values['-CODDEPOSITO-']
        input4_value = values['-DESCRDEPOSITO-']
        input2_value = values['-CODPRODOTTO-']
        input2_value = values['-DESCRPRODOTTO-']
        input2_value = values['-DATAENTRATA-']
        input2_value = values['-DATAUSCITA-']
        input2_value = values['-SALDOINIZIALE-']
        input2_value = values['-DISPONIBILITA-']
        sg.popup(f'Inseriti : Cod. causale: {input1_value}, Descrizione: {input2_value}, Cod. causale2 {input3_value}, Tipo movimento {input4_value}')
# Chiude la finestra
window.close()
