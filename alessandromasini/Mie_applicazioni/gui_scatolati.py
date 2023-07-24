

import PySimpleGUI as sg


sg.theme('Dark Blue 3')  

layout = [[sg.Text('LISTA PEZZI:', justification='left', size=(28,1)),
           sg.Text('LISTA SCATOLATI:', justification='right', size=(30,1),expand_x=True)],
          [sg.Listbox(values=[], size=(30, 6), key='-BARRE-',horizontal_scroll=True,expand_x=True,expand_y=True),
           sg.Listbox(values=[], size=(30, 6), key='-LISTABARRE-',horizontal_scroll=True,expand_x=True,expand_y=True)],
          [sg.Text('Lunghezza:'),sg.Input(key='-LUNGHEZZA-',size=(10,1)),
           sg.Text('Quantità: '),sg.Input(key = '-QUANTITA-', size=(10,1))],
          [sg.Button('Aggiungi')],
          [sg.Button('Calcola'),sg.Text(key='-CALCOLO-',size=(30,1))],
          [sg.Button('Esci')]
        ]


window = sg.Window('CALCOLO BARRE', layout, enable_close_attempted_event=True, resizable=True,size=(640,480))

lista_pezzi = []
pezzi = []

while True:  
    event, values = window.read()
    print(event, values)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Esci') and sg.popup_yes_no('Vuoi uscire?') == 'Yes':
        break
    elif event == 'Aggiungi':
        if values["-LUNGHEZZA-"] == "" or values["-QUANTITA-"] == "":
            sg.popup("Inserisci dei valori")
        else:    
            try:
                lung = float(values['-LUNGHEZZA-'])
                qta = float(values['-QUANTITA-'])
                for i in range(int(qta)):
                    pezzi.append(lung)
                lista_pezzi.insert(0, pezzi)
                window["-BARRE-"].update(lista_pezzi)
                window["-LUNGHEZZA-"].update("")
                window["-QUANTITA-"].update("")
                pezzi = []
            except:
                sg.popup("Inserisci dei numeri")

    elif event == 'Calcola':
        for pezzo in lista_pezzi:
            print(pezzo)
            lista_singola = []
            for sublist in lista_pezzi:
                lista_singola.extend(sublist)
            

        barre =     []

        lista_new = []
        
        cont = 0


        while len(lista_singola) > 0:
            for i in range(0, len(lista_singola)):
                massimo = max(lista_singola)
                if (sum(lista_new) + massimo) <= 6000:
                    lista_singola.remove(massimo)
                    lista_new.append(massimo)
                else:
                    break

            for i in range(0, len(lista_singola)):
                minimo = min(lista_singola)
                if (sum(lista_new) + minimo) <= 6000:
                    lista_singola.remove(minimo)
                    lista_new.append(minimo)
                else:
                    break    
            
            barre.insert(cont, lista_new)
            cont = cont + 1
            lista_new = []

        if len(barre) > 1:
            messaggio = (f"Servono: {len(barre)} barre da 6000")
            #print(messaggio)
        else:
            messaggio = (f"Serve: {len(barre)} barra da 6000")
            #print(messaggio)

        window["-LISTABARRE-"].update(barre)
        window["-CALCOLO-"].update(messaggio)
        

window.close()
























