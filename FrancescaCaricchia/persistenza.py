from mytables import metaobj, user, causale
from create_engine import engine

metaobj.create_all(bind= engine) 
#gli dico che deve crearlo sul mio engine
#cosi mi scrive in sql la struttura dati, mi crea tabella
#mi crea tutto quello che ho creato in mytables con l'engine creato precedentemente.
#creo engine, creo classi, metto in metadata, chiedo che venga consolidato l'oggetto.
#da ora uso python per fare tutto (tanto c'è sqlalchemy che traduce)