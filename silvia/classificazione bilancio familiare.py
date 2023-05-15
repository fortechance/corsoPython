#classificazione bilancio familiare
#1.identifico le classi: conto corrente, benefit, investimenti

from typing import Any


tipoentrata = {"emolumenti", "assegnounico", "competenze", "affittiricevuti", "ricavititoli", "pensioneinvalidità", "altraentrata"}

class Contocorrente():
    def __init__(self, entrate, uscite, risparmio):
       self.entrate = entrate
       self.uscite = uscite
       self.risparmio = risparmio

class Benefit():
   def __init__(self, entratebenefit, uscitebenefit, risparmiobenefit):
       self.entratebenfit = entratebenefit
       self.uscitebenefit = uscitebenefit
       self.risparmiobenefit = risparmiobenefit
      

class Investimenti():
   def __init__(self, versamento, disinvestimento, capitaleinvestito):
      self.versamento = versamento
      self.disinvestiemnto = disinvestimento
      self.capitaleinvestito = capitaleinvestito

class Entrate():
    def __init__(self, tipoentrata, data):
       self.tipoentrata = tipoentrata
       self.data = data
       

#oppure:


class Entrate():
    def __init__(self,emolumenti, assegnounico, competenze, affittiricevuti, alimentiricevuti, ricavititoli, pensioneinvalidità, altraentrata):
      self.emolumenti = emolumenti
      self.assegnounico = assegnounico
      self.competenze = competenze
      self.affittiricevuti =affittiricevuti
      self.alimentiricevuti = alimentiricevuti
      self.ricavititoli = ricavititoli
      self.pensioneinvalidità = pensioneinvalidità
      self.altraentrata = altraentrata

class Uscite():
   def __init__(self, affitto, mutuo, finanziamento, spesaalimentare, cena, pranzo, palestra, cartadicreditomeseprec, altreuscite):
      
