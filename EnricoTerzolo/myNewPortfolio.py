from myEngine import engine
from myTables import portfolio, wallet, tipowallet , causale, movimento

from sqlalchemy import Insert, Select

import PySimpleGUI as ps

import datetime

def doNewMouvement(wall):

    with engine.connect() as cn:

        s = Select(causale)
        cau = cn.execute(s).all()
        listcau=[]

        for c in cau:

            listcau.append(f'{c[0]} - ({c[1]}) {c[2]}')

        '''
        Importo, causale
        dtmovimento,descrizione
        
        '''

        layout = [
            [ps.Text('Importo: '),ps.Input(key = '-importo-'), ps.Text('Causale: '), ps.Combo(listcau,key = '-causale-')],
            [ps.Text('', key = '-dtmov-'), ps.CalendarButton('Data Movimento',target = '-CALENDAR-', key = '-CALENDAR-', format = '%Y-%m-%d'), ps.Text('Descrizione: '),ps.Input(key = '-descrizione-')],
            [ps.HorizontalSeparator()],
            [ps.Button('OK'), ps.Button('Annulla')]
        ]

        window = ps.Window('Inserimento Movimento', layout, modal = True)

        while True:

            events, values = window.read()

            if events == ps.WIN_CLOSED or events == 'Annulla': 
                break
            elif events == 'OK':
                 
                errori = 0
                
                imp = values['-importo-']
                cau = values['-causale-']
                des = values['-descrizione-']
                dtm = values['-CALENDAR-']
                wal = wall

                i = Insert(movimento).values(
                    
                    IMPORTO = imp,
                    CAUSALE = cau[:3],
                    DTMOVIMENTO = dtm,
                    DESCRIZIONE = des,
                    IDWALLET = wal
                )

                try:

                    cn.execute(i)
                    cn.commit()
                    break
                
                except Exception as e:
                    cn.rollback()
                    ps.popup(e.__str__)
                    continue
        
        window.close()

                
def doNewWallet(idPortfolio):

    with engine.connect() as cn:

        s = Select(tipowallet)
        walletType = cn.execute(s).all()
        listTipoW = []

        for w in walletType:          
            listTipoW.append(f'{w[0]} - {w[1]} [{w[2]}]')

        listFV = ['F - Fisico', 'V - Virtuale']

        layout = [

            [ps.Text('Inserisci il nome del Wallet: '), ps.Input(key = '-nomeWallet-')],
            [ps.Text('Inserisci il Tipo Wallet: '), ps.Combo(values = listTipoW, key = '-TipoWallet-')],
            [ps.Text('Inserisci se Fisico o Virtuale'), ps.Combo(values = listFV, key = '-walletFV-')],
            [ps.Button('OK'),ps.Button('Annulla')]

        ]

        window = ps.Window('Inserimento nuovo Wallet', layout, modal = True)

        while True:

            events, values = window.read()

            if events == ps.WIN_CLOSED or events == 'Annulla': 
                break

            elif events == 'OK':
                
                descrizione = values['-nomeWallet-']
                tpwallet = values['-TipoWallet-'][:3]
                fv = values['-walletFV-'][0]
                portfolio = int(idPortfolio)

                i = Insert(wallet).values(
                    DESCRIZIONE = descrizione,
                    TIPOWALLET = tpwallet,
                    FV = fv,
                    IDPORTFOLIO = portfolio
                    )
                
                cn.execute(i)
                try:                    
                    cn.commit()
                    break
                except Exception as e:
                    cn.rollback()
                    ps.popup(e.__str__)
                    continue
                
        
        window.close()



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
    