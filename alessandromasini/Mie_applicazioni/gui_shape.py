import PySimpleGUI as sg
from shape import Shape,Rectangle,Square,Triangle,Circle,Hexagon



sg.set_options(font=('Arial Bold', 16))

layout = [
        [sg.Text("Calcolo area:")],
        [sg.Button("Rettangolo")],
        [sg.Button("Quadrato")],
        [sg.Button("Triangolo")],
        [sg.Button("Cerchio")],
        [sg.Button("Esagono")],
        [sg.Text("Lato Quadrato",key="-TEXTLATOQUADRATO-",visible=False),sg.Input(key="-LATOQUADRATO-",size=(6,1),visible=False),
         sg.Text("Base Triangolo",key="-TEXTBASETRIANGOLO-",visible=False),sg.Input(key="-BASETRIANGOLO-",size=(6,1),visible=False),
         sg.Text("Raggio",key="-TEXTRAGGIO-",visible=False),sg.Input(key="-RAGGIO-",size=(6,1),visible=False),
         sg.Text("Altezza",key="-TEXTALTEZZA-",visible=False),sg.Input(key="-ALTEZZA-",size=(6,1),visible=False),
         sg.Text("Lato A",key="-TEXTLATO1-",visible=False),sg.Input(key="-LATO1-",size=(6,1),visible=False),
         sg.Text("Lato B",key="-TEXTLATO2-",visible=False),sg.Input(key="-LATO2-",size=(6,1),visible=False),
         sg.Text("Lato Esagono",key="-TEXTLATOESAGONO-",visible=False),sg.Input(key="-LATOESAGONO-",size=(6,1),visible=False)
        ],
        [sg.Text("Area",key="-TEXTAREA-",visible=False),sg.T("Risultato",key="-RISULTATO-",visible=False)],
        [sg.Button("Calcola Rettangolo",key="-CALCOLARETTANGOLO-",visible=False),
         sg.Button("Calcola Quadrato",key="-CALCOLAQUADRATO-",visible=False),
         sg.Button("Calcola Triangolo",key="-CALCOLATRIANGOLO-",visible=False),
         sg.Button("Calcola Cerchio",key="-CALCOLACERCHIO-",visible=False),
         sg.Button("Calcola Esagono",key="-CALCOLAESAGONO-",visible=False)
        ],
        [sg.Cancel()]
        ]
            

window = sg.Window("My APP", layout,size=(640,480))


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
      break
    
    
    elif event == "Rettangolo":

        window["-TEXTLATOQUADRATO-"].update(visible=False)
        window["-LATOQUADRATO-"].update(visible=False)
        window["-TEXTRAGGIO-"].update(visible=False)
        window["-RAGGIO-"].update(visible=False)
        window["-TEXTALTEZZA-"].update(visible=False)
        window["-ALTEZZA-"].update(visible=False)
        window["-TEXTBASETRIANGOLO-"].update(visible=False)
        window["-BASETRIANGOLO-"].update(visible=False)
        window["-TEXTLATO1-"].update(visible=True)
        window["-LATO1-"].update(visible=True)
        window["-TEXTLATO2-"].update(visible=True)
        window["-LATO2-"].update(visible=True)
        window["-TEXTLATOESAGONO-"].update(visible=False)
        window["-LATOESAGONO-"].update(visible=False)
        window["-TEXTAREA-"].update(visible=True)
        window["-RISULTATO-"].update(visible=True)
        window["-CALCOLARETTANGOLO-"].update(visible=True)
        window["-CALCOLAQUADRATO-"].update(visible=False)
        window["-CALCOLATRIANGOLO-"].update(visible=False)
        window["-CALCOLACERCHIO-"].update(visible=False)
        window["-CALCOLAESAGONO-"].update(visible=False)
        window['-RISULTATO-'].update("")

    elif event == "Quadrato":

        window["-TEXTLATOQUADRATO-"].update(visible=True)
        window["-LATOQUADRATO-"].update(visible=True)
        window["-TEXTRAGGIO-"].update(visible=False)
        window["-RAGGIO-"].update(visible=False)
        window["-TEXTALTEZZA-"].update(visible=False)
        window["-ALTEZZA-"].update(visible=False)
        window["-TEXTBASETRIANGOLO-"].update(visible=False)
        window["-BASETRIANGOLO-"].update(visible=False)
        window["-TEXTLATO1-"].update(visible=False)
        window["-LATO1-"].update(visible=False)
        window["-TEXTLATO2-"].update(visible=False)
        window["-LATO2-"].update(visible=False)
        window["-TEXTLATOESAGONO-"].update(visible=False)
        window["-LATOESAGONO-"].update(visible=False)
        window["-TEXTAREA-"].update(visible=True)
        window["-RISULTATO-"].update(visible=True)
        window["-CALCOLARETTANGOLO-"].update(visible=False)
        window["-CALCOLAQUADRATO-"].update(visible=True)
        window["-CALCOLATRIANGOLO-"].update(visible=False)
        window["-CALCOLACERCHIO-"].update(visible=False)
        window["-CALCOLAESAGONO-"].update(visible=False)
        window['-RISULTATO-'].update("")

    elif event == "Triangolo":

        window["-TEXTLATOQUADRATO-"].update(visible=False)
        window["-LATOQUADRATO-"].update(visible=False)
        window["-TEXTRAGGIO-"].update(visible=False)
        window["-RAGGIO-"].update(visible=False)
        window["-TEXTBASETRIANGOLO-"].update(visible=True)
        window["-BASETRIANGOLO-"].update(visible=True)
        window["-TEXTALTEZZA-"].update(visible=True)
        window["-ALTEZZA-"].update(visible=True)
        window["-TEXTLATO1-"].update(visible=False)
        window["-LATO1-"].update(visible=False)
        window["-TEXTLATO2-"].update(visible=False)
        window["-LATO2-"].update(visible=False)
        window["-TEXTLATOESAGONO-"].update(visible=False)
        window["-LATOESAGONO-"].update(visible=False)
        window["-TEXTAREA-"].update(visible=True)
        window["-RISULTATO-"].update(visible=True)
        window["-CALCOLARETTANGOLO-"].update(visible=False)
        window["-CALCOLAQUADRATO-"].update(visible=False)
        window["-CALCOLATRIANGOLO-"].update(visible=True)
        window["-CALCOLACERCHIO-"].update(visible=False)
        window["-CALCOLAESAGONO-"].update(visible=False)
        window['-RISULTATO-'].update("")

    elif event == "Cerchio":

        window["-TEXTLATOQUADRATO-"].update(visible=False)
        window["-LATOQUADRATO-"].update(visible=False)
        window["-TEXTRAGGIO-"].update(visible=True)
        window["-RAGGIO-"].update(visible=True)
        window["-TEXTALTEZZA-"].update(visible=False)
        window["-ALTEZZA-"].update(visible=False)
        window["-TEXTBASETRIANGOLO-"].update(visible=False)
        window["-BASETRIANGOLO-"].update(visible=False)
        window["-TEXTLATO1-"].update(visible=False)
        window["-LATO1-"].update(visible=False)
        window["-TEXTLATO2-"].update(visible=False)
        window["-LATO2-"].update(visible=False)
        window["-TEXTLATOESAGONO-"].update(visible=False)
        window["-LATOESAGONO-"].update(visible=False)
        window["-TEXTAREA-"].update(visible=True)
        window["-RISULTATO-"].update(visible=True)
        window["-CALCOLARETTANGOLO-"].update(visible=False)
        window["-CALCOLAQUADRATO-"].update(visible=False)
        window["-CALCOLATRIANGOLO-"].update(visible=False)
        window["-CALCOLACERCHIO-"].update(visible=True)
        window["-CALCOLAESAGONO-"].update(visible=False)
        window['-RISULTATO-'].update("")

    elif event == "Esagono":

        window["-TEXTLATOQUADRATO-"].update(visible=False)
        window["-LATOQUADRATO-"].update(visible=False)
        window["-TEXTRAGGIO-"].update(visible=False)
        window["-RAGGIO-"].update(visible=False)
        window["-TEXTALTEZZA-"].update(visible=False)
        window["-ALTEZZA-"].update(visible=False)
        window["-TEXTBASETRIANGOLO-"].update(visible=False)
        window["-BASETRIANGOLO-"].update(visible=False)
        window["-TEXTLATO1-"].update(visible=False)
        window["-LATO1-"].update(visible=False)
        window["-TEXTLATO2-"].update(visible=False)
        window["-LATO2-"].update(visible=False)
        window["-TEXTLATOESAGONO-"].update(visible=True)
        window["-LATOESAGONO-"].update(visible=True)
        window["-TEXTAREA-"].update(visible=True)
        window["-RISULTATO-"].update(visible=True)
        window["-CALCOLARETTANGOLO-"].update(visible=False)
        window["-CALCOLAQUADRATO-"].update(visible=False)
        window["-CALCOLATRIANGOLO-"].update(visible=False)
        window["-CALCOLACERCHIO-"].update(visible=False)
        window["-CALCOLAESAGONO-"].update(visible=True)
        window['-RISULTATO-'].update("")
    
    elif event == "-CALCOLARETTANGOLO-":
             
      lato1rect = float(values['-LATO1-'])
      lato2rect = float(values['-LATO2-'])
      rec = Rectangle(lato1rect, lato2rect)
      risultato = rec.get_area()
      risultato = round(risultato,2)
      window['-RISULTATO-'].update(risultato)

    elif event == "-CALCOLAQUADRATO-":
           
      window['-RISULTATO-'].update("")
      latoqua = float(values['-LATOQUADRATO-'])
      qua = Square(latoqua)
      risultato = qua.get_area()
      risultato = round(risultato,2)
      window['-RISULTATO-'].update(risultato)


    elif event == "-CALCOLATRIANGOLO-":
            
        window['-RISULTATO-'].update("")
        base = float(values['-BASETRIANGOLO-'])
        altezza = float(values['-ALTEZZA-'])
        tri = Triangle(base,altezza)
        risultato = tri.get_area()
        risultato = round(risultato,2)
        window['-RISULTATO-'].update(risultato)

    elif event == "-CALCOLACERCHIO-":
           
      window['-RISULTATO-'].update("")
      raggio = float(values['-RAGGIO-'])
      cer = Circle(raggio)
      risultato = cer.get_area()
      risultato = round(risultato,2)
      window['-RISULTATO-'].update(risultato)

    elif event == "-CALCOLAESAGONO-":
           
      window['-RISULTATO-'].update("")
      latoesagono = float(values['-LATOESAGONO-'])
      esa = Hexagon(latoesagono)
      risultato = esa.get_area()
      risultato = round(risultato,2)
      window['-RISULTATO-'].update(risultato)


