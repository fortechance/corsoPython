from myEngine import engine
from myTables import portfolio, wallet, tipowallet 

from sqlalchemy import Insert, Select

import PySimpleGUI as ps



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
            tipowallet = values['-TipoWallet-'][0][:3]
            fv = values['-walletFV-'][0][:1]
            portfolio = idPortfolio

            i = Insert(wallet).values(
                DESCRIZIONE = descrizione,
                TIPOWALLET = tipowallet,
                FV = fv,
                IDPORTFOLIO = portfolio
                )
            
            cn.execute(i)
            cn.commit()


            






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
    