import json
class utente:
  
  def __init_(self, CodUtente, nome, cognome, età):
    self.nome = nome
    self.cognome = cognome
    self.eta = età
    self.CodUtente = CodUtente

class causale:
  def __init__(self, CODCAUSALE, DESCRIZIONE, SEGNO):
    self.CODCAUSALE = CODCAUSALE
    self.DESCRIZIONE = DESCRIZIONE
    self.SEGNO = SEGNO

class tipowallet:
  def __init__(self, CodWallet, Wallet):
    self.Codwallet = CodWallet
    self.wallet = Wallet
#lahcen = utente()
#lahcen.nome = "lahcen"
#print(lahcen.nome)
#import json
NomeFile = 'LahcenOuhas/utente1.csv'
Separatore = ';'
with open(NomeFile,'r') as pippo:
    #f.write("ciao")

    buffer = pippo.read()

#print(buffer)

righe = buffer.split('\n')
#print(righe)
#print(len(righe))

#priKey = 0
dictDati = {}
dictCampi = {}

DaScrivere = ""

for riga in righe:
   if (len(riga) > 1):
        colonne = riga.split(Separatore)
        if len(colonne) != 4:
            print("Separatore errato")
        else:
            if (colonne[0]=='CodUtente' and colonne[1] =='Nome' and colonne[2] =='Cognome' and colonne[3] =='età'):
                #titoli delle colonne, li salto
                pass 
            else:
             user = utente()
 
             user.CodUtente = colonne[0]
             user.nome = colonne[1]
             user.cognome = colonne[2]
             user.età = colonne[3]
            
             
            dictCampi[user.cognome] =  {'CodUtente': user.CodUtente , 'Nome': user.nome,'cognome' : user.cognome,'eta' : user.età}

print(dictCampi)


dictCausale = {}

for riga in righe:
   if (len(riga) > 1):
        colonne = riga.split(Separatore)
        if len(colonne) != 4:
            print("Separatore errato")
        else:
            if (colonne[0]=='Cognome' and colonne[1] =='Nome'):
                #titoli delle colonne, li salto
                pass 
            else:
             user = utente()
 
             user.CodUtente = colonne[0]
             user.nome = colonne[1]
             user.cognome = colonne[2]
             user.età = colonne[3]
            
             dictCausale[user.cognome] =  {'CodUtente': user.CodUtente , 'Nome': user.nome,'cognome' : user.cognome,'eta' : user.età}
print(dictCausale)
 