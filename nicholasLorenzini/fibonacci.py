import math

def ap(raggio):

    area = AreaCerchio(raggio)
    perimetro = 2*raggio*math.pi

    return (area,perimetro)

def AreaCerchio(raggio):
    area = raggio*raggio*math.pi

    return area
#serie di fibonacci
#times = input("quante volte?")
def fibonacci(numero): #funzione / Libreria
    sequenza = []
    a = 0
    b = 1

    for i in range(numero):
        fibo = a + b
        a = b
        b = fibo
        
        sequenza.append(fibo)
    return sequenza
#print(fibonacci(times))