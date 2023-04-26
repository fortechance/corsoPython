#serie di fibonacci


sequenza ={}
def fibonacci(numero):
 
 primo = 0
 secondo = 1

 for i in range(10):
   fibonacci = primo + secondo
   primo = secondo
   secondo = fibonacci

   print(fibonacci)
   sequenza.append(fibonacci)
  
 return sequenza
print(fibonacci(5))


 



