import PySimpleGUI as sg

layout = [
    [sg.Text("Seleziona una data:")],
    [sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Cal US No Buttons Location (0,0)', target='-IN-')],
    [sg.Button('Ok'), sg.Button('Annulla')]
]



window = sg.Window('Calendario', layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Annulla':
        break
    elif event == 'Ok':
        selected_date = values['-DATE-']
        print(f'Hai selezionato la data: {selected_date}')

window.close()
