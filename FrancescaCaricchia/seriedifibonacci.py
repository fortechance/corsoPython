a = 0
b = 1
for i in range(10):
    c=a+b
    a=b
    b=c
    print(c)

a = 1
b = 0
for i in range(10):
    c=a+b
    b=c
    if a!=b:
        a=b
    print(c)