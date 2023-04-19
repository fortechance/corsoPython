

def Fibonacci(numero):

#Fibonacci 

   sequenza = {}

   primo =0
   secondo =1

   for i in range (numero):
     
       Fibonacci = primo + secondo
       primo = secondo
       secondo = Fibonacci


       print (Fibonacci)
       sequenza.append(Fibonacci)

   return sequenza

#questo è lo scritp che mi interessa
print(Fibonacci(5))