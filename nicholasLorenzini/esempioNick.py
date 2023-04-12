#importo la libreria per data e ora
import datetime as dt

nome = "Nick"
#stampiamo a video ciao, corso python
print ("ciao, corso Python")
#richiamare una variabile in una stringa (f)
print (f"Io sono {nome}")

#assegno alla variabile dataOrario tutta la data e ora ecc. now è la funzione, datetime è la classe / metodo
dataOrario = dt.datetime.now()
#stampa data e ora ecc.
print (f"sono le {dataOrario}")

#voglio stampare solo orario (ora:minuto:secondo)
orarioGiusto = f"{dataOrario.hour}:{dataOrario.minute}:{dataOrario.second}"
print (f"in realtà sono le {orarioGiusto}")

#lo faccio con una tupla
orarioGiusto2 = (f"{dataOrario.hour}:{dataOrario.minute}:{dataOrario.second}")
print (f"in realtà sono le {orarioGiusto2}")

#mi faccio domandare come mi chiamo in input
tuoNome = input("come ti chiami?")
test = input("Sei sicuro?")
if (test=="no"):
    tuoNome = input("Allora come tichiami?")
    test2 = input("No, tu ti chiami Giobbe. è corretto?")
    if (test2=="si"):
        print("Ciao Giobbe")
    else:
        print(tuoNome)    
else:
    pass