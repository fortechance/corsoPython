import PySimpleGUI as sg
import csv

sg.set_options(font=('Arial Bold', 16))
def create_dictionary(file_path):
    dictionary = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            value = row[1]
            dictionary[key] = value
    return dictionary

# Definisci il layout dell'interfaccia grafica
layout = [
    [sg.Text('Seleziona il file log taglio di tipo CSV')],
    [sg.Input(), sg.FileBrowse(button_text='     Cerca    ', button_color='#4da6ff')],
    [sg.Text('_' * 56)],
    [sg.Text(' ' * 78), sg.Submit(button_text='Conferma', button_color=('white', '#FF8DC7')), sg.Cancel(button_text='Uscita', button_color=('white' , '#4da6ff'))]
]

# Crea la finestra
window = sg.Window('Caricamento log CSV lavorazione lab. taglio in Dizionario', layout)

# Event loop per interagire con la finestra
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Cancel'):
        break
    elif event == 'Submit':
        file_path = values[0]
        dictionary = create_dictionary(file_path)
        sg.popup('Il file CSV è stato caricato nel dizionario con successo!')
        print(dictionary)

# Chiudi la finestra
window.close()
