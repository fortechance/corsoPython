a = 0
b = 1
for i in range(10):
    c=a+b
    a=b
    if b!=c:
        b=c
    print(c)