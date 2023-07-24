coffee=4
tea=3
coke=2
print()
menu={'Coffee':'$4.00','Tea':'$3.00','Coca-cola':'$2.00',"Press 'd' ":"complete order"}
ccount=0
tcount=0
cokecount=0
while True:
    for i in menu:
        print(f"{i}={menu[i]}")
    print()
 
 
    Condition=True
    while(Condition):
        drink=input('Select your drink from the menu:')
        drink=drink.capitalize()
 
        if drink == 'Coffee':
              quantity=int(input('Quantity:'))
              ccount+=quantity
              Condition=False
        elif drink == 'Tea':
             quantity=int(input('Quantity:'))
             tcount+=quantity
             Condition=False
        elif drink == 'Coca-cola':
             quantity=int(input('Quantity:'))
             cokecount+=quantity
             Condition=False
 
        elif drink=='D':
            condition=False
            amount=( ccount*4)+(tcount*3)+(cokecount*2)
            mem=input('Do u have membership?( Enter Y for yes, N for no):')
            mem=mem.capitalize()
            if amount>=10 and mem=='Y':
                purchaseDisc=amount*0.05
                memDisc=(amount-purchaseDisc)*0.15
                befTotal=(amount-purchaseDisc-memDisc)
                gst=befTotal*0.07
                total=befTotal+gst
 
            elif amount<10 and mem=='Y':
                purchaseDisc=0
                memDisc=amount*0.15
                befTotal=amount-memDisc
                gst=befTotal*0.07
                total=befTotal+gst
 
            elif amount>=10 and mem=='N':
                purchaseDisc=amount*0.05
                memDisc=0
                befTotal=amount-purchaseDisc
                gst=befTotal*0.07
                total=befTotal+gst
 
            else:
                purchaseDisc=0
                memDisc=0
                befTotal=amount
                gst=befTotal*0.07
                total=befTotal+gst
 
 
            print()
            print('Receipt')
            print('==============================')
            print(f'{"Drink":5s}:               {drink:>1s}')
            print(f'{"Quantity":8s}:{quantity:>13}')
            print(f'{"Member":6s}:{mem:>15}')
            print(f'{"Amount":6s}:{"$":>15}{amount:>5.2f}')
            print(f'{"Purchase Disc.":14s}{"$":>8}{purchaseDisc:>5.2f}')
            print(f'{"Member Disc.":12s}{"$":>10}{memDisc:>5.2f}')
            print(f'{"Total (bef. GST)":16s}{"$":>6}{befTotal:>5.2f}')
            print(f'{"GST":3s}{"$":>19}{gst:>5.2f}')
            print(f'{"Total (incl. GST)":17s}{"$":>5}{total:>5.2f}')
            exit()
        else:
             print('Please enter a drink from the menu!')
             Condition=True