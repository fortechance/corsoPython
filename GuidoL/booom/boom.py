class utente:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class famiglia:      
    def __init__(self,nome_famiglia) -> None:
        self.famiglia=nome_famiglia
        self.componenti_famiglia=[]
        
    def add_member(self,fam:utente):
        self.componenti_famiglia.append(fam)  
        
        
##############################TRANSAZIONI###########################
  
class transazione:
    def __init__(self,value, valuta,data):
        self.value = value
        self.valuta = valuta
        self.data = data
 
class transazione_IN(transazione):
    def __init__(self,categoria_IN, value, valuta, data):
        self.categoria_IN=categoria_IN
        super().__init__(value, valuta, data)
    
class transazione_OUT(transazione):
    def __init__(self,categoria_OUT, value, valuta, data):
        self.categoria_OUT=categoria_OUT
        super().__init__(value, valuta, data)


   
class transazione_fondo(transazione):
    def __init__(self,categoria_Fondo, value, valuta, data):
        self.categoria_Fondo=categoria_Fondo
        
        def gestisce_la_disponibilità():
            pass
        super().__init__(value, valuta, data)
     
#########################CATEGORIE##############################à 


#gestire macro e micro categorie da classi?
class categorie_IN:
     pass
 
 
class categorie_OUT:
    pass
 
#########################COLLETTORI####################################à    
class entrate:
    def __init__(self,ut:utente) -> None:
        self.utente=ut
        self.trans_IN=[]
        
    def add_transaction(self,tr:transazione_IN):
        self.trans_IN.append(tr)
        
class uscite:
    def __init__(self,ut:utente) -> None:
        self.utente=ut
        self.trans_OUT=[]
        
    def add_transaction(self,tr:transazione_OUT):
        self.trans_OUT.append(tr)
        
        
    #_____________________conti______________________#
    
      
class conti: #potrei avere piu conti, banche, carte di credito/debito
    def __init__(self,) -> None:
        pass       
    
class banca(conti): 
    def __init__(self,nome_conto,) -> None:
    
        super().__init__()
        
class contanti(conti): 
    def __init__(self) -> None:
        super().__init__()
      
class carta_di_credito(conti): 
    def __init__(self,valuta) -> None:
        
        super().__init__()
        
