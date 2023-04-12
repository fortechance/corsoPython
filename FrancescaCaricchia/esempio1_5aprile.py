import datetime
#oppure import datetime as pippo, e poi la richiamo con pippo e sotto scriverò orario = pippo.datetime.now()
#questo è un commento
#queste scritte sono il primo esercizio in python

nome = "francesca"
#oppure sotto posso scrivere orario = dt.datetime.now()
orario = datetime.datetime.now()
orarioOK = (orario.hour, orario.minute, orario.second)
anni = "26.5 quasi 27"

print(f"ho {anni} anni")
print("ciao, corso python")
print("il tuo nome è francesca")
print(f"il tuo nome è {nome}")
print(f"sono le {orario}")
print(f"no in realtà sono le {orarioOK}")

#mi faccio chiedere come mi chiamo. quello che scrivo dentro input viene poi usato per stampare la variabile con quello che ho scritto. lo vedo dopo averlo inserito il risultato del mio input
nome = input("come ti chiami?")
print(f"il tuo nome è {nome}")
print(f"il tuo nome è {nome}")

test = input("sei sicuro?")
if (test=="no"):
	nome = input("ripeti")
else: 
	pass