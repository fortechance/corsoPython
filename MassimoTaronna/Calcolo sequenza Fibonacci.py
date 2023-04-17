# Programma per visualizzare la sequenza di Fibonacci per n iterazioni
# A1 = 0                    primo numero sequenza di Fibonacci
# A2 = 1                    secondo e terzo numero sequenza di Fibonacci
# An = A(n-1) + A(n-2)      ennesimo numero sequenza di Fibonacci

# richiesta di quanti numeri della sequenza vogliamo visualizzare
n_iter = int(input("Quante iterazioni? "))

# primi due numeri della sequenza
A1, A2 = 0, 1
count = 0

# controlla che il numero delle iterazioni sia valido
if n_iter <= 0:
   print("Inserire un numero intero positivo")
# se c'è solo un'interazione restituisci A1
elif n_iter == 1:
   print("Sequenza di Fibonacci:")
   print(A1)
# genera la sequenza di Fibonacci
else:
   print("Sequenza di Fibonacci:")
   while count < n_iter:
       print(A1)
       An = A1 + A2
       # aggiorna valori
       A1 = A2
       A2 = An
       count += 1
