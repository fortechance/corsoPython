#questo è lo script (programma) che usa le classi 

from condominiecase import quartiere, condominio, casa, attico
import os

nomeCSV = 'csvCondominio.csv'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#path = BASE_DIR + "AlessandroF" #per windows
#nomeCSV = path + "\\" + nomeCSV # per windows
#per il mac il path è così:
nomeCSV = BASE_DIR + "/20230503/" + nomeCSV

q = quartiere(nomeCSV)
#per esempio vogliosapereimillesimidiun appartamento

c:condominio = q.condominio['condominioA']

amill = c.calcolaMillesimi('A1')

print (f'millesinmi di A1: {amill}')