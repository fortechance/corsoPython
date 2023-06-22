from myEngine import engine
from myTables import portfolio
from sqlalchemy import Insert

import PySimpleGUI as ps

def doNewPortfolio(codowner):
    
    layout =[
        [ps.Text('Inserisci il nome del Porfolio')],
        [ps.Input(key = '-descrportfolio-')],
        [ps.Button('OK'),ps.Button('Annulla')]
    ]

    window = ps.Window('Inserimento Portfolio',layout, modal = True)

    while True:

        events, values = window.read()

        if events == ps.WIN_CLOSED or events == 'Annulla': 
            break
        elif events == 'OK':
            # inserimento dati in DB

            descr = values['-descrportfolio-']
            
            if len(descr)==0:
                ps.popup("valorzzare la descrizione.")
                continue

            statement = Insert(portfolio).values(DESCRIZIONE = descr, OWNER = codowner)
            with engine.connect() as cn:
                
                cn.execute(statement)
            
                try:
                    cn.commit()
                    break  

                except Exception() as e:
                    cn.rollback()
                    ps.popup(e.__str__)

    window.close()
    