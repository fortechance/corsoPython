#import Fibonacci
#import math
from Fibonacci import AreaCerchio, fibonacci, ap

numeri=(fibonacci(10))


print(numeri)

for n in numeri:
    area=AreaCerchio(n)
    area=round(area,2)
    print(f'Area= {area}')

    ar, pe = ap(n)

    print (f'area e perimetro = {ar,pe}')
    arpe = ar*pe

    print(f'Dato inutile: {arpe}')



