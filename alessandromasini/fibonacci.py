# creo primi 10 numeri sequenza di Fibonacci

a = 0
b = 1

for i in range(0,10):

    c = a + b
    a = b
    b = c

    print(c)


