import PySimpleGUI as sg


menu = [
       ["File",["New file", "Open", "Save", "---", "Exit"]],
       ["Edit", ["Copy", "Paste", "Maiuscolo", "Minuscolo"]],
       ["Help", ["Help", "Tutorial", "About"]]
       ]

Col_1 = [
        [sg.Multiline(key="-MULTIA-", size=(35,20))]
        ]

Col_2 = [
        [sg.Multiline(key="-MULTIB-", size=(35,20))]
        ]

layout = [
        [sg.Menu(menu, key="-MENU-")],
        [sg.Col(Col_1), sg.VerticalSeparator(), sg.Col(Col_2)],
        [sg.Button("MAIUSCOLO")],
        [sg.Button("MINUSCOLO")],
        [sg.Cancel()]
        ]

windows = sg.Window("Created by Alessandro Masini ", layout, size=(640,480))


while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED or event == "Cancel"or event == "Exit":
        break
    elif event == "MAIUSCOLO" or event == "Maiuscolo":
        testo = values["-MULTIA-"]
        testo_upper = testo.upper()
        windows["-MULTIB-"].update(testo_upper)
    elif event == "MINUSCOLO" or event == "Minuscolo":
        testo = values["-MULTIA-"]
        testo_lower = testo.lower()
        windows["-MULTIB-"].update(testo_lower)
    elif event == "About":
        sg.popup("""
        Questa APP
        è stata creata
        da Alessandro Masini
        """)
        
windows.close()

# esempio
# windows['-OUTPUT-'].update(values['-IN-'])