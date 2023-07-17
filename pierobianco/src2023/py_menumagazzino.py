import PySimpleGUI as sg

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
    [sg.Button(image_filename="F:\img2023\lg2023.png", image_size=(70, 30), border_width=0, button_color=('white') ), sg.Text("                 MENU' GESTIONE MAGAZZINO                    ")],
    [sg.HorizontalSeparator()],
    [sg.Button(image_filename="F:\icone_2023\prodotti.png", image_size=(40, 40), border_width=0),
     sg.Button("ANAGRAFICA PRODOTTI", size=(25, 1), button_color=('white', '#4da6ff')  ), sg.Text(" ", size=(20, 1))],
    [sg.Button(image_filename="F:\icone_2023\depositi.png", image_size=(40, 40), border_width=0),
     sg.Button("ANAGRAFICA DEPOSITI", size=(25, 1),button_color=('white', '#4da6ff') ), sg.Text(" ", size=(20, 1))],
    [sg.Button(image_filename="F:\icone_2023\causali.png", image_size=(40, 40), border_width=0),
     sg.Button("CAUSALI MOVIMENTAZIONE", size=(25, 1),button_color=('white', '#4da6ff') ), sg.Text(" ", size=(20, 1))],
    [sg.Button(image_filename="F:\icone_2023\giacenze.png", image_size=(40, 40), border_width=0),
     sg.Button("GIACENZE", size=(25, 1),button_color=('white', '#4da6ff') ), sg.Text(" ", size=(20, 1))],
    [sg.Button(image_filename="F:\icone_2023\movimenti.png", image_size=(40, 40), border_width=0),
     sg.Button("MOVIMENTI", size=(25, 1),button_color=('white', '#4da6ff') ), sg.Text(" ", size=(20, 1))],
    [sg.Button(image_filename="F:\icone_2023\grafici48c.png", image_size=(40, 40), border_width=0),
     sg.Button("GRAFICI  -  STATISTICHE", size=(25, 1),button_color=('white', '#4da6ff') ), sg.Text(" ", size=(20, 1))],
    [sg.Button(image_filename="F:\icone_2023\inpexp48.png", image_size=(40, 40), border_width=0),
     sg.Button("IMPORT - EXPORT DATI", size=(25, 1),button_color=('white', '#4da6ff') ), sg.Text(" ", size=(20, 1))],
    # Aggiungi i bottoni per le altre applicazioni...
    [sg.HorizontalSeparator()],
    [sg.Button('Uscita', button_color=('white', '#FF8DC7', ))]
]

# Crea la finestra principale con il layout del menu
window = sg.Window("MENU' GESTIONE MAGAZZINO", menu_layout, element_justification='center')

# Ciclo principale dell'applicazione
while True:
    event, _ = window.read()

    # Gestisci gli eventi dei bottoni
    if event == sg.WINDOW_CLOSED or event == "Esci":
        break
    elif event == "Rilevazione misure":
        applicazione_1()
    elif event == "Magazzino":
        applicazione_2()
    elif event == "Etichette":
        applicazione_3()
    elif event == "Vendite":
        applicazione_4()
    elif event == "Portfolio":
        applicazione_5()
    elif event == "Grafici - Statistiche":
        applicazione_6()

# Chiudi la finestra al termine dell'applicazione
window.close()
