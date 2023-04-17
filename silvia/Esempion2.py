#Esempio n.2

a=34

if (a==10):
    print("Vale 10")
else:
    print("Non vale 10")



while True:

    nome = input("come ti chiami? ")   
    test = input("sei sicuro? ")

    if (test=="s"):
        print(f"il tuo nome è {nome}")
        break
    else:
        print("Non ho capito il tuo nome")

print("Ciclo di richiesta nome eseguito")
