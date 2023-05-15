



class utente:
    def __init__(self, name):
        self.name = name
        
################USER######################        
class famiglia:      
    def __init__(self,nome_famiglia) -> None:
        self.famiglia=nome_famiglia
        self.componenti_famiglia=[]
        
    def add_member(self,fam:utente):
        self.componenti_famiglia.append(fam)  
###################WALLET#########################à
class wallet:
    def __init__(self,descrizione,u:utente) -> None:
        self.user=u
        self.descrizione=descrizione
        self.movimenti=[]  
        
class conto_corrente(wallet):
    def __init__(self,nome_banca, descrizione, u: utente) -> None:
        self.nome_banca=nome_banca
       
        self.movimenti=[] 
        self.valuta= None #!!!!!!!!!!!!!!da gestire (Stesso gg movimento)
        
        super().__init__(descrizione, u)

###############Causali################à

class causale:
    def __init__(self,descrizione,from_wall,to_wall) -> None:
        self.descrizione=descrizione
        self.from_wall=from_wall
        self.to_wall=to_wall
 
 
 ###############Movimenti ################à

        
class movimento:
    def __init__(self,c:causale,importo,data,) -> None:
        self.importo=importo
        self.data=data
        self.from_wall=c.from_wall
        self.to_wall=c.to_wall
        
""" class movimento_IN(movimento):
    def __init__(self, c: causale, from_wall,to_wall,importo, data) -> None:        
        self.to_wall=to_wall
        super().__init__(c, importo, data) """



#class movimento_OUT(movimento):



#class movimento_TRANS(movimento):




#_____________________________________________________________#
u=utente("Bob")
f=famiglia("famiglia di Bob").add_member(u)
w=conto_corrente("Banca d'italia","nienta da dichiarare",u)


c1=causale("cose mie")
m1=movimento_IN(c1,"",w,15,"10/12/23")

