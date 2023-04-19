import math

def ap(raggio):

    area = AreaCerchio(raggio)
    perimetro = 2*raggio*math.pi

    return (area,perimetro)

def AreaCerchio(raggio):
    area = raggio*raggio*math.pi

    return area



def fibonacci(numero):

#Fibonacci
    sequenza = []

    primo =0
    secondo =1

    for i in range(numero):

        fibonacci = primo + secondo 
        primo = secondo
        secondo = fibonacci

       # print(fibonacci)
        sequenza.append(fibonacci)

    return sequenza

#questo è lo script che mi interessa
#print(Fibonacci())


