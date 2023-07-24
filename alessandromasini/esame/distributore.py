import PySimpleGUI as sg
import csv
import os


sg.theme('Dark Blue 3')  
sg.set_options(font=('Arial Bold', 14))


ricette = ['GinTonic', 'Mojito', 'Negroni', 'RumCola']

Col_1 = [
        [sg.Text('PRODOTTI:', justification='left', size=(30,1),pad=(8,8))],
        [sg.Listbox(values=[], size=(40, 15), key='-PRODOTTI-',horizontal_scroll=True,expand_x=True,expand_y=True)],
        [sg.Button('CARICA PRODOTTI',pad=(8,8))]
        ]

Col_2 = [
        [sg.Text('COCKTAIL:', justification='left', size=(30,1),pad=(8,8))],
        [sg.Listbox(values=[], size=(40, 15), key='-COCKTAIL-',horizontal_scroll=True,expand_x=True,expand_y=True)],
        [sg.Button('CARICA COCKTAIL',pad=(8,8))]
        ]

layout = [
        [sg.Col(Col_1), sg.VerticalSeparator(), sg.Col(Col_2)],
        [sg.Text('COCKTAIL:', justification='left', size=(10,1),pad=(8,8)),
            sg.Combo(ricette, key="-COMBO-", size=(10,1),pad=(8,8), default_value=ricette[0]),
            sg.Text('Quantità: '),sg.Input(key = '-QUANTITA-', size=(10,1),pad=(8,8))],
        [sg.Button('Ordina',pad=(8,8)),sg.Text(key='-ORDINA-',size=(35,1),pad=(8,8), background_color='white', text_color='black')],
        [sg.Button('Esci',pad=(8,8))]
        ]

window = sg.Window('DISTRIBUTORE DEL SORRISO', layout, enable_close_attempted_event=True, resizable=True)



while True:  
    event, values = window.read()
    print(event, values)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Esci') and sg.popup_yes_no('Vuoi uscire?') == 'Yes':
        break

    elif event == 'CARICA PRODOTTI':

        basepath = os.getcwd()
        file_csv = '\\prodotti.csv'
        file_path = basepath + '\\alessandromasini\\esame' + file_csv

     
        with open(file_path, newline='') as csvfile_prodotti:
            lettore_prodotti = csv.DictReader(csvfile_prodotti)
        
            dati_prodotti = []
            for riga in lettore_prodotti:
                dati_prodotti.append(riga)   

     
        window["-PRODOTTI-"].update(dati_prodotti)

    elif event == 'CARICA COCKTAIL':

        basepath = os.getcwd()
        file_csv = '\\ricette.csv'
        file_path = basepath + '\\alessandromasini\\esame' + file_csv

        with open(file_path, newline='') as csvfile:
            lettore = csv.DictReader(csvfile)

            dati = []
            dati_ricette = []
            cont = 0
            for riga_ricette in lettore:
                dati.append(riga_ricette)
                nome = dati[cont]['nome']
                id1 = dati[cont]['id1']
                tot1 = dati[cont]['tot1']
                id2 = dati[cont]['id2']
                tot2 = dati[cont]['tot2']
                id3 = dati[cont]['id3']
                tot3 = dati[cont]['tot3']
                inserisci_ricette = (f" {nome} = {id1}:{tot1} / {id2}:{tot2} / {id3}:{tot3}")
                dati_ricette.append(inserisci_ricette)
                cont = cont + 1
     
        window["-COCKTAIL-"].update(dati_ricette) 
    elif event == 'Ordina':
        
        basepath = os.getcwd()
        file_csv_prodotti = '\\prodotti.csv'
        file_path = basepath + '\\alessandromasini\\esame' + file_csv_prodotti

        with open(file_path, newline='') as csvfile_prodotti:
            lettore_prodotti = csv.DictReader(csvfile_prodotti)
        
            dati_prodotti = []
            for riga in lettore_prodotti:
                dati_prodotti.append(riga)
                
            
        basepath = os.getcwd()
        file_csv_ricette = '\\ricette.csv'
        file_path = basepath + '\\alessandromasini\\esame' + file_csv_ricette

        with open(file_path, newline='') as csvfile_ricette:
            lettore_ricette = csv.DictReader(csvfile_ricette)

            dati_ricette = []
            for riga in lettore_ricette:
                dati_ricette.append(riga)

            
        
      
        selected_option = values['-COMBO-']

        if selected_option == ricette[0]:
            qta = values['-QUANTITA-']
            dati_prodotti[0]['totale'] = (int(dati_prodotti[0]['totale'])) - (int(dati_ricette[0]['tot2'])) * int(qta)
            if dati_prodotti[0]['totale'] < 0:
                sg.popup("Hai esaurito l'acquatonica")
                window["-QUANTITA-"].update(0)
            dati_prodotti[4]['totale'] = (int(dati_prodotti[4]['totale'])) - (int(dati_ricette[0]['tot1'])) * int(qta)
            if dati_prodotti[4]['totale'] < 0:
                sg.popup("Hai esaurito il Gin")
                window["-QUANTITA-"].update(0)     
            window["-PRODOTTI-"].update(dati_prodotti)

            lista_ordina = (f" Hai ordinato {qta} {selected_option}")

            window["-ORDINA-"].update(lista_ordina)

        elif selected_option == ricette[1]:
            qta = values['-QUANTITA-']
            dati_prodotti[7]['totale'] = (int(dati_prodotti[7]['totale'])) - (int(dati_ricette[1]['tot1'])) * int(qta)
            if dati_prodotti[7]['totale'] < 0:
                sg.popup("Hai esaurito il Rum")
                window["-QUANTITA-"].update(0)
            dati_prodotti[5]['totale'] = (int(dati_prodotti[5]['totale'])) - (int(dati_ricette[1]['tot2'])) * int(qta)
            if dati_prodotti[5]['totale'] < 0:
                sg.popup("Hai esaurito il Lime")
                window["-QUANTITA-"].update(0)
            dati_prodotti[9]['totale'] = (int(dati_prodotti[9]['totale'])) - (int(dati_ricette[1]['tot3'])) * int(qta)
            if dati_prodotti[9]['totale'] < 0:
                sg.popup("Hai esaurito la Soda")
                window["-QUANTITA-"].update(0)


            window["-PRODOTTI-"].update(dati_prodotti)

            lista_ordina = (f" Hai ordinato {qta} {selected_option}")

            window["-ORDINA-"].update(lista_ordina)

        elif selected_option == ricette[2]:
            qta = values['-QUANTITA-']
            dati_prodotti[2]['totale'] = (int(dati_prodotti[2]['totale'])) - (int(dati_ricette[2]['tot1'])) * int(qta)
            if dati_prodotti[2]['totale'] < 0:
                sg.popup("Hai esaurito il Campari")
                window["-QUANTITA-"].update(0)
            dati_prodotti[4]['totale'] = (int(dati_prodotti[4]['totale'])) - (int(dati_ricette[2]['tot2'])) * int(qta)
            if dati_prodotti[4]['totale'] < 0:
                sg.popup("Hai esaurito il Gin")
                window["-QUANTITA-"].update(0)
            dati_prodotti[6]['totale'] = (int(dati_prodotti[6]['totale'])) - (int(dati_ricette[2]['tot3'])) * int(qta)
            if dati_prodotti[6]['totale'] < 0:
                sg.popup("Hai esaurito il MartiniRosso")
                window["-QUANTITA-"].update(0)

            window["-PRODOTTI-"].update(dati_prodotti)

            lista_ordina = (f" Hai ordinato {qta} {selected_option}")

            window["-ORDINA-"].update(lista_ordina)

        elif selected_option == ricette[3]:
            qta = values['-QUANTITA-']
            dati_prodotti[7]['totale'] = (int(dati_prodotti[7]['totale'])) - (int(dati_ricette[3]['tot1'])) * int(qta)
            if dati_prodotti[7]['totale'] < 0:
                sg.popup("Hai esaurito il Rum")
                window["-QUANTITA-"].update(0)
            dati_prodotti[3]['totale'] = (int(dati_prodotti[3]['totale'])) - (int(dati_ricette[3]['tot2'])) * int(qta)
            if dati_prodotti[3]['totale'] < 0:
                sg.popup("Hai esaurito la Cocacola")
                window["-QUANTITA-"].update(0)

            window["-PRODOTTI-"].update(dati_prodotti)

            lista_ordina = (f" Hai ordinato {qta} {selected_option}")

            window["-ORDINA-"].update(lista_ordina)

window.close()