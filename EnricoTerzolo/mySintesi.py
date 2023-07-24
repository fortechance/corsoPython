#sintesi!

from myEngine import engine
from myTables import *
import PySimpleGUI as sg
from sqlalchemy import Select
from myRefresh import RefreshMouvements
import datetime


def Sintesi(idWallet):

    movs = RefreshMouvements(idWallet, True)

    movim = []

    totale = 0

    for m in movs:
        imp = m.IMPORTO
        seg = m.SEGNO
        dat = m.DTMOVIMENTO

        if seg == '-':
            imp = imp * -1


        totale += imp
        movim.append(f'{dat}, {imp}')


        print(seg, imp, dat)

    movim.append(f'{datetime.date.today()}, {totale}')    
    return movim


    



