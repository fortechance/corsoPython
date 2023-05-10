#usiamo i nostri bei files dove 
#abbiamo definito le classi ad esempio
#Fattura, Cliente, ecc. ecc.4

from cFattura import *
import datetime

#leggo da un db a caso un elenco articoli
#e un elenco clienti

c = cliente('cliente1', 12345678901,'qqqwww55e22l219c',0,0)
f = fattura(c,1,datetime.datetime.today(),0)
a = articolo(1,'carta da pacchi',3,22,'pz')
df = dettagliofattura(a,10,0)

f.aggiungiRiga(df)



 
