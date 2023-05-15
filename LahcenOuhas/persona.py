class Persona:
  def __init__(self, nome, età, sesso, job):
    self.nome = nome
    self.età = età
    self.sesso = sesso
    self.job = job
  def presentati(self):
    print(f"Ciao, mi chiamo {self.nome} e ho {self.età} anni")
    print(f"sono sistemista di rete {self.job}")

p = Persona("Lahcen", 25, "maschio", "")
p.presentati()  # Ciao, mi chiamo lahcen e ho 25 anni, sono sistemista di rete