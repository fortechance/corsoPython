from condominioecase import *
import os #per gestire i path

nomeCsv = "condominioA.csv"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print (f"Il percorso è {BASE_DIR}") #c:\Users\Utente\Desktop\corsoPython

percorso = BASE_DIR + "\\EnricoTerzolo" #il doppio slash serve per annullare gli apici
nomeCsv = percorso + "\\" + nomeCsv

q = quartiere(nomeCsv)

c:condominio = q.condomini["condominioA"]
aMill = c.calcoloMillesimi("A1")

print(f"I millesimi di A1 sono: {aMill}")
print(f"i condomini sono: {len(q.condomini)}")

for condominio in q.condomini:
    print(f"il condominio {condominio} ha {len(q.condomini)} appartamenti")

