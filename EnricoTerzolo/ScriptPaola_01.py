from classiWallet import *

eCau = causali()

try:
    c = causale('stipendio','+')
    eCau.AddCausale(c)
    c = causale('Mutuo','-')
    eCau.AddCausale(c)
    #questo genera un errore:
    c= causale('lotteria', '+')
    eCau.AddCausale(c)
    c= causale('Riscossione Affitto', '+')
    eCau.AddCausale(c)

except:
    print(f'causale {c.descrizione} duplicata')

try:

    cc = causale('Stipendio','+')
    m=movimento(cc,2000,eCau)
    
except:
    print(f'causale {cc.descrizione} non esiste')


