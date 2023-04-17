from math import sqrt
def Fib(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))     # formula per il calcolo del numero di Fibonacci

def Fibonacci(n_iniz, n_fine):
    n = 0
    cur = Fib(n)
    while cur <= n_fine:
        if n_iniz <= cur: 
            print (int(cur))
        n += 1
        cur = Fib(n)
Fibonacci (1, 1000)