#apro il ciclo while
nome = input("Come ti chiami?")
seiSicuro = input("Sei sicuro?")
if seiSicuro=="SI":
    print(f"Ciao, {nome}")
elif seiSicuro=="NO":
    while seiSicuro=="NO":
        nome = input("Allora come ti chiami?")
        seiSicuro = input("Sei sicuro?")
        if seiSicuro=="SI":
            print(f"Ciao, {nome}")
            break
        else:
            print("Cazzo!")
else:
    print("Tu non hai un nome!")
#Ciclo for
for eta in range(18,36):
    print(eta) #stampa da 18 a 35?
#secondo ciclo
lista = [1,2,3,4,5]
for n in lista:
    print(n) #stampa 1 2 3 4 5 