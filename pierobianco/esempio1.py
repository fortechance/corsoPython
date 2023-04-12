import datetime as pippo
# questo è un commento
# primo esercizio in python
nome = "Pippo"
nome = input ("Come ti chiami ?")

test = input("Sei sicuro *")
if (test=="n"):
	nome = input("Ripeti")
else:
	pass


orario = pippo.datetime.now()
# orarioOK = dattime.strptimeformat(orario.format("%h-%m-%s")
orarioOK = (orario.hour, orario.minute, orario.second)
print("Ciao , corso python")
print(f"il tuo nome è {nome}")
print(f"Sono le {orario}")
print(f"ora sono le {orarioOK}")