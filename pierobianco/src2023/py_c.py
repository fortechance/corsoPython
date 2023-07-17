import PySimpleGUI as sg
from pynput import keyboard

sg.set_options(font=('Arial Bold', 16))

# Definisci il dizionario con le coppie chiave-valore delle causali
causali_data = {
    "EN": "ENTRATA",
    "US": "USCITA",
    "CA": "CARICO",
    "SC": "SCARICO",
    "RT": "ROTTAMAZIONE"
}

# Definisci il dizionario per memorizzare gli inserimenti delle causali
inserimenti_causali = {}

# Definisci il layout della finestra principale
layout_main = [
    [sg.Button(image_filename="F:\img2023\lg2023.png", image_size=(70, 30), border_width=0, button_color=('white')),
     sg.Text("                 GESTIONE CAUSALI DI MOVIMENTAZIONE MAGAZZINI           ")],
    [sg.HorizontalSeparator()],
    [sg.Text(" ")],
    [sg.Text('Cod. causale      :'), sg.Input(size=(2, 1), key='-CAUSALE-', enable_events=True),
     sg.Text(''), sg.Input(size=(40, 1), key='-DESCRIZIONE-')],
    [sg.Text('Tipo movimento  :'), sg.Input(size=(1, 1), key='-TIPO-', tooltip='E=Entrata U=Uscita A=Altro'),
     sg.Text("    E=Entrata U=Uscita A=Altro")],
    [sg.Text(" ")],
    [sg.HorizontalSeparator()],
    [sg.Button('Inserisci', button_color=('white', '#FF8DC7')),
     sg.Button('Variazione', button_color=('white', '#FFACC7')),
     sg.Button('Cancella', button_color=('white', 'orange')),
     sg.Button('Stampa', button_color=('white', '#FFC6C2')),
     sg.Button('Esporta-csv', button_color=('white', '#AEE2FF')),
     sg.Button('Conferma', button_color=('white', '#62A8D1')),
     sg.Button('Uscita', button_color=('white', '#93C6E7'))]
]

# Definisci il layout della finestra della listbox
layout_listbox = [
    [sg.Button(image_filename="F:\img2023\lg2023.png", image_size=(70, 30), border_width=0, button_color=('white')),
     sg.Text('                ELENCO CAUSALI', font=('Arial Bold', 16))],
    [sg.Listbox(values=[f"{k} - {v}" for k, v in causali_data.items()], text_color="#4da6ff", size=(40, 6),
                key='-LISTBOX-', enable_events=True)]
]

# Crea le finestre
window_main = sg.Window('Causali di movimentazione', layout_main)
window_listbox = sg.Window('Lista Causali', layout_listbox, finalize=True)
window_listbox.hide()

# Variabili per tracciare lo stato del tasto F2 e la visibilità della finestra della listbox
f2_pressed = False
listbox_visible = False

# Funzione di callback per il rilevamento del tasto F2
def on_key_press(key):
    global f2_pressed
    if key == keyboard.Key.f2:
        f2_pressed = True

def on_key_release(key):
    global f2_pressed
    if key == keyboard.Key.f2:
        f2_pressed = False

# Crea l'ascoltatore dei tasti
listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
listener.start()

# Loop principale per gestire gli eventi
while True:
    event_main, values_main = window_main.read()
    event_listbox, values_listbox = window_listbox.read(timeout=0)

    # Controllo degli eventi della finestra principale
    if event_main == sg.WINDOW_CLOSED or event_main == 'Uscita':
        break
    elif event_main == 'Conferma':
        input1_value = values_main['-CAUSALE-']
        input2_value = values_main['-DESCRIZIONE-']
        input3_value = values_main['-TIPO-']

        if input3_value.upper() in ['E', 'U', 'A']:
            tipo_movimento = causali_data.get(input3_value.upper(), 'Altro')

            # Memorizza gli inserimenti delle causali nel dizionario
            inserimenti_causali[input1_value] = {'descrizione': input2_value, 'tipo_movimento': tipo_movimento}

            sg.popup(
                f'Inseriti : Cod. causale: {input1_value}, Descrizione: {input2_value}, Tipo movimento: {tipo_movimento}')
        else:
            sg.popup('Errore: Tipo movimento non valido. Inserire solo "E", "U" o "A".')

    # Controllo degli eventi della finestra della listbox
    if event_listbox == '-LISTBOX-':
        selected_causale = values_listbox['-LISTBOX-'][0].split(" - ")[0]
        window_main['-CAUSALE-'].update(selected_causale)

    # Controllo dello stato del tasto F2 e la visibilità della finestra della listbox
    if f2_pressed and not listbox_visible:
        window_listbox.un_hide()
        listbox_visible = True
    elif not f2_pressed and listbox_visible:
        window_listbox.hide()
        listbox_visible = False

# Termina l'ascoltatore dei tasti
listener.stop()

# Chiude le finestre
window_main.close()
window_listbox.close()

# Stampa il dizionario degli inserimenti delle causali
print(inserimenti_causali)
EN