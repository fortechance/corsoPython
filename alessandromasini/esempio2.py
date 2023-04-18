a = 10

if (a==10):
    print("Vale 10")

else:
    print("Non vale 10")

while True:
    nome = input("Come ti chiami? ")

    test = input("Sei sicuro? ")

    if (test=="s"):
        print(f"il tuo nome e' {nome}")
        break
    else:
        print("Non ho capito il tuo nome")
        
print("Ciclo eseguito")