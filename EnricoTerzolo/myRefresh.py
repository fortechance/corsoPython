from myEngine import engine
from sqlalchemy import Select
from myTables import *



def RefreshMouvements(idWallet, data = False):

    with engine.connect() as cn:

        joinCondition = movimento.c.CAUSALE == causale.c.CODICE

        s= Select(movimento, causale).select_from(causale.join(movimento, joinCondition)).filter(movimento.c.IDWALLET == idWallet)

#        s = Select( movimento, causale, wallet).where(
#            movimento.c.IDWALLET == wallet.c.ID and
#            movimento.c.CAUSALE[:3] == causale.c.CODICE[:3]
#        ).filter(wallet.c.ID == idWallet)
                
        listamovimenti = cn.execute(s).all()
        
        movlist = []
        for m in listamovimenti:
            movlist.append(f'{m[0]} - [{m[3].date()}] - € {m[8]}{m[1]} - <{m[7]}>:{m[4]}')


    if data:
        return listamovimenti
    else:
        return movlist

def RefreshWallet(idportfolio, data = False):

    with engine.connect() as cn:

        s = Select(wallet).where(wallet.c.IDPORTFOLIO == idportfolio)
        walletlist = cn.execute(s).all()

        wallets = []
        walletsq = {}

        rownumber = 0

        for w in walletlist:
            wallets.append(f'{w[0]} - {w[1]}')

            walletsq[w[0]] = {}
            walletsq[w[0]]['ID'] = w[0]
            walletsq[w[0]]['DESCRIZIONE0'] = w[1]

    if data:
        return walletsq
    else:
        return wallets
    

def RefreshPorfolio(cut, query: bool = False):

    with engine.connect() as cn:

        s = Select(portfolio).where(portfolio.c.OWNER == cut)
        portlist = cn.execute(s).all()
        
        valori = []
        valoriq  = {}

        rownumber = 0
        for p in portlist:

            valori.append(f'{p[0]} - {p[1]}')
            
            valoriq[p[0]] = {}
            valoriq[p[0]]['DESCRIZIONE'] = p[1]
            valoriq[p[0]]['OWNER'] = p[2]

            rownumber +=1

    if query:
        return valoriq
    else:
        return  valori
