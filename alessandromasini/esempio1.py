import datetime as pippo

# commento : questo è un commento


# queste scritte sono il primo esercizio di python

#nome = "Alessandro"

nome = input("Come ti chiami?")

test = input("Sei sicuro?")

if (test=="n"):
    nome = input("Ripeti")

    print("Nome verificato")

orario = pippo.datetime.now()

orarioOK = (orario.hour, orario.minute, orario.second)


print("Ciao, corso Python")
print(f"il tuo nome è {nome}")
print(f"Sono le {orario}")
print(f"in realtà sono le {orarioOK}")
