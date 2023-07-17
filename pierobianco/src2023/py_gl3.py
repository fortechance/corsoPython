import matplotlib.pyplot as plt

# Dati
mesi = ['Gen', 'Feb', 'Mar', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
valori2023 = [150000, 250000, 300000, 550000, 45000, 150000, 50000, 650000, 95000, 1000000, 120000]
valori2022 = [50000, 20000, 30000, 50000, 45000, 10000, 350000, 65000, 9500, 10000, 12000]
valori2021 = [15000, 25000, 35000, 25000, 45000, 15000, 5000, 6500, 9500, 10000, 12000]

# Creazione del grafico a linee
plt.plot(mesi, valori2021, marker='o', label='2021')
plt.plot(mesi, valori2022, marker='o', label='2022')
plt.plot(mesi, valori2023, marker='o', label='2023')

# Configurazione dell'asse y come scala logaritmica
plt.yscale('log')

# Aggiunta di etichette agli assi e al titolo
plt.xlabel('Mesi')
plt.ylabel('Valore')
plt.title('Confronto valori mensili per anni')
plt.legend()

# Mostra il grafico
plt.show()
