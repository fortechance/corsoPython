import matplotlib.pyplot as plt

# Dati
mesi = ['Gen', 'Feb', 'Mar', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
valori = [150000, 250000, 300000, 550000, 45000, 150000, 50000, 650000, 95000, 1000000, 120000]

# Creazione del grafico a barre
plt.bar(mesi, valori)

# Configurazione dell'asse y come scala logaritmica
plt.yscale('log')

# Aggiunta di etichette agli assi e al titolo
plt.xlabel('Mesi')
plt.ylabel('Valore')
plt.title('Grafico a barre dei valori mensili')

# Mostra il grafico
plt.show()
