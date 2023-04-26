#Fibonacci terzarolo
def funzioneFibonacci(numero):    #funzione fibonacci con N volte che deve ciclare

    sequenza = []

    primo = 0
    secondo =1

    for i in range(numero):
        fibonacci = primo + secondo
        primo = secondo
        secondo = fibonacci

        print(fibonacci)         #printa mano a mano che li calcola
        sequenza.append(fibonacci)    #i dati calcolati li accoda (append) ad una sequenza
    return sequenza


#############
print(funzioneFibonacci(20)) #il 20 è il nunero di cicli  #volendo sipuò commentare questo print e farlo in un file a parte
# basta fare un file con import "nomefile" ed poi con - from nomefile import nomefunzione epoi a capo print(fibonacci(10)) nel nuovo file fa ilprint


