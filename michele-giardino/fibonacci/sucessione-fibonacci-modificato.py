# Chiediamo all'utente di inserire il numero di elementi della successione che vuole calcolare
n = int(input("Inserisci il numero di elementi della successione di Fibonacci che vuoi calcolare: "))

# Inizializziamo i primi due numeri della successione
a, b = 0, 1

# Stampiamo il primo elemento della successione (0)
print(a)

# Stampiamo il secondo elemento della successione (1)
print(b)

# Calcoliamo gli elementi successivi e li stampiamo
for i in range(2, n):
    c = a + b
    print(c)
    # Dopo aver stampato c dati dei nuovi valori ad a e b
    a = b
    b = c
