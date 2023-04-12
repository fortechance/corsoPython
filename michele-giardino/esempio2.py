import datetime as pippo

# commento: questo è un esercizio in python

#nome = "Enrico"

nome = input("Come ti chiami?")

test= input("Sei sicuro? ")

if (test=='n'):
	nome = input("Ripeti ")

	print("Nome verificato")
	ssse="Ho verifocato la if"
	print(ssse)



orario = pippo.datetime.now()
orarioOK = (orario.hour, orario.minute, orario.second)

print("ciao, Corso di Python")
print(f"il tuo nome è {nome}")
print(f"Sono le {orario}")
print(f"in realtà sono le {orarioOK}")

while True:
	
	nome = input("come ti chiami?")
	test = input("sei sicuro?")

	if (test=="s"):
		print(f"il tuo nome è {nome}")
		break
	else:
		print("Non ho capito il tuo nome")
		
print("Ciclo di richiesta nome eseguito")