# esempio ciclo if

a = 12
if (a==10):
    print("Vale 12")
else:
    print("Non Vale 12")
# ciclo while True esegue le istruzioni all'infinito ricominciando da capo ogni volta
#
# potevo scrivere 
# continuapersempre = true
# While continuapersempre:
#
# per terminare il ciclo 


while True:  
    nome=input("come ti chiami?")
    test= input("sei sicuro")

    if (test=="s"):
        print("il tuo nome  è {nome}")
        break
    else:
        print("non ho capito il tuo nome")
print("Bravo, hai finito")


