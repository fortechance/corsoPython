n = int(input('Quanti numeri di Fibonacci?: ' ))        # richiesta di quanti numeri vogliamo la sequenza
a = 0                                                   # primo numero
b = 1                                                   # secondo numero
print(a)                                                # visualizza il primo numero
print(b)                                                # visualizza il secondo numero

for i in range(n):                                      # ciclo for eseguito n volte
    c=a+b                                               # calcolo numero successivo sequenza
    a=b                                                 
    b=c
    print(c)