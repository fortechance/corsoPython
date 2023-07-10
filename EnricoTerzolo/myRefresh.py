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

def RefreshWallet(idportfolio):

    with engine.connect() as cn:

        s = Select(wallet).where(wallet.c.IDPORTFOLIO == idportfolio)
        walletlist = cn.execute(s).all()

        wallets = []
        for w in walletlist:
            wallets.append(f'{w[0]} - {w[1]}')

    return wallets


def RefreshPorfolio(cut):

    with engine.connect() as cn:

        s = Select(portfolio).where(portfolio.c.OWNER == cut)
        portlist = cn.execute(s).all()
        
        valori = []

        for p in portlist:

            valori.append(f'{p[0]} - {p[1]}')
           
        return  valori
