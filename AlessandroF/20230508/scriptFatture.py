
#importiamo il file dando from file import  e non import file perchè la seconda 
#modalità la usiamo solo in caso dilibreria di python

from cFattura import *
#import datetime

c = cliente('cliente1', 123459012,'codfiscale','contanti','2%' )
f = fattura(c,1,datetime.datetime.today(),0)
a = articolo(1,'carta da pacchi', 3,22,'pz')
df = dettagliofattura(a,10,0)

f.aggiungiRiga(df)
