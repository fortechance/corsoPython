import PySimpleGUI as sg
import os

basepath = os.path.dirname(__file__)
basepath = os.path.join(basepath, '..\\img2023')
sg.set_options(font=('Arial Bold', 16))

# Definisci le funzioni per le applicazioni associate alle selezioni del menu
def applicazione_1():
    print("Applicazione 1")

def applicazione_2():
    print("Applicazione 2")

def applicazione_3():
    print("Applicazione 3")

def applicazione_4():
    print("Applicazione 4")

def applicazione_5():
    print("Applicazione 5")

def applicazione_6():
    print("Applicazione 6")

# Crea il layout del menu
menu_layout = [
    [sg.Button(image_filename=f"{basepath}\\lg2023.png", image_size=(70, 30), border_width=0, button_color=('white') ),
    sg.Text(" MENU' APPLICAZIONI", justification='left')],
    [sg.HorizontalSeparator()],
    [
        sg.Button(image_filename=f"{basepath}\\misure482.png", image_size=(40, 40), border_width=0),
        sg.Button("RILEVAZIONE MISURE", size=(23, 1), button_color=('white', '#4da6ff') )
    ],
    [
        sg.Button(image_filename=f"{basepath}\\muletto42c.png", image_size=(40, 40), border_width=0),
        sg.Button("MAGAZZINO", size=(23, 1), button_color=('white', '#4da6ff') )
    ],
    [
        sg.Button(image_filename=f"{basepath}\\etichette4822.png", image_size=(40, 40), border_width=0),
        sg.Button("GESTIONE ETICHETTE", size=(23, 1), button_color=('white', '#4da6ff') )
    ],
    [
        sg.Button(image_filename=f"{basepath}\\shop48c.png", image_size=(40, 40), border_width=0),
        sg.Button("VENDITE", size=(23, 1), button_color=('white', '#4da6ff') )
    ],
    [
        sg.Button(image_filename=f"{basepath}\\portfolio48c.png", image_size=(40, 40), border_width=0),
        sg.Button("PORTFOLIO", size=(23, 1), button_color=('white', '#4da6ff') )
    ],
    [
        sg.Button(image_filename=f"{basepath}\\grafici48c.png", image_size=(40, 40), border_width=0),
        sg.Button("GRAFICI  -  STATISTICHE", size=(23, 1), button_color=('white', '#4da6ff') )
    ],
    [
        sg.Button(image_filename=f"{basepath}\\inpexp48.png", image_size=(40, 40), border_width=0),
        sg.Button("IMPORT - EXPORT DATI", size=(23, 1), button_color=('white', '#4da6ff') )
    ],
    # Aggiungi i bottoni per le altre applicazioni...
    [sg.HorizontalSeparator()],
    [sg.Text(' ' * 180), sg.Button('Dashboard', button_color=('white', '#4da6ff')),
    sg.Button('Uscita', button_color=('white', '#FF8DC7'))],
    ## [sg.Text("IMMAGINE", justification='right')],
    [sg.HorizontalSeparator()],
    [sg.Button(image_filename=f"{basepath}\\modit20.png", image_size=(1300, 550), border_width=0)]
]

# Crea la finestra principale con il layout del menu
window = sg.Window("MENU' APPLICAZIONI", menu_layout, element_justification='left')

# Ciclo principale dell'applicazione
while True:
    event, _ = window.read()

    # Gestisci gli eventi dei bottoni
    if event == sg.WINDOW_CLOSED or event == "Uscita":
        break
    elif event == "RILEVAZIONE MISURE":
        applicazione_1()
    elif event == "MAGAZZINO":
        applicazione_2()
    elif event == "GESTIONE ETICHETTE":
        applicazione_3()
    elif event == "VENDITE":
        applicazione_4()
    elif event == "PORTFOLIO":
        applicazione_5()
    elif event == "GRAFICI  -  STATISTICHE":
        applicazione_6()

# Chiudi la finestra al termine dell'applicazione
window.close()
