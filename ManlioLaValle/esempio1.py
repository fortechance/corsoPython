import datetime

nome = "Cattivix"
orario = datetime.datetime.now()
#obj = datetime.now()
#orarioOK = obj.strftime("%HH-%mm-%ss")

# richiamo la libreria datetime e lo chiamo pippo.datetime.now()
#orario = pippo.datetime.now()  

nome = input("come ti chiami?")
test = input("sei sicuro?")
if (test=="n"):
	nome = input("Ripeti")
else:
	pass
print("ciao,pippo")
print(f"il più cattivo è {nome}")
print(f"sono le {orario}")
#print(f"in realtà sono le {orarioOK}")  #in questo caso uso  un unica stringa
print("sono le:", orario)   #in questo caso uso la tupla

s=f'fsgds'   # stringa forattata, per passare le variabili
# tutto quello che segue è come scrivere print(f"tu ti chiami" {nome})
ss = 'tu ti chiami'
ss = ss + nome
print(ss)

#Domanda: posso richiamare la variabile puntualmente oppure con "f"
#import datetime 
#	oppure
#from datetime import datetime

