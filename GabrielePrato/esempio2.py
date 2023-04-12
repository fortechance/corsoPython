#esempio 2

a=10

if(a==10):
    print("vale 10")
else:
    print("non vale 10")

while True:
    nome=input("come ti chiami?")
    test=input("sei sicuro?")

    if(test=="s"):
        print(f"il tuo nome è {nome}")
        break
    else:
        print("Non ho capito il tuo nome")

print("finito ciclo while")