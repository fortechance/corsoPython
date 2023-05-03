# questo è lo script (programma) che usa le classi

from condominioecase import quartiere, condominio, casa, attico
import os

nomeCSV = 'condominioA.csv'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

path = BASE_DIR + "\\EnricoTerzolo"
nomeCSV = path + "\\" + nomeCSV

q = quartiere(nomeCSV)

#per esempio voglio sapere i millesimi di un appartamento di un 
#condominio del quartiere

c:condominio = q.condomini['condominioA']

amill = c.calcolaMillesimi('A1')

print (f'millesimi di A1: {amill}')
print (f'condomini: {len(q.condomini)}')
for cc in q.condomini:
    print(f'Condominio: {cc}')
    print (len(q.condomini[cc].elencoCase))



