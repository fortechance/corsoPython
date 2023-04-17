#the librarie of TIMER
import datetime
import time
import datetime as pippo

#this is the comment
#this write code are first esercice in python

nome = "BERNARD"
orario = pippo.datetime.now()

nam = input("what is your name")

test = input("are you sure\t")

orarioOK = (orario.hour, orario.minute, orario.second)

if (test == "n"):
    	nome = input("#############---->>>>>ripeti")
else:
	pass
	print("nome verificato\t")




print("ciao , corso python")
print(f"this is my {nome}{test}")		 #--->this f mean that the string a dd should be implemented
print(f"this are time {orario}")

print(f"----------------------------------------------->this are time {orarioOK}")

print("without f-------------------------------------->",orario)

print("your name is \t",nam)

