import numpy as np
import matplotlib.pyplot as plt

# Dati
mesi = ['Gen', 'Feb', 'Mar', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']

valori2023 = [150000, 250000, 300000, 550000, 45000, 150000, 50000, 650000, 95000, 1000000, 120000]
valori2022 = [50000, 20000, 30000, 50000, 45000, 10000, 350000, 65000, 9500, 10000, 12000]
valori2021 = [15000, 25000, 35000, 25000, 45000, 15000, 5000, 6500, 9500, 10000, 12000]

# Larghezza delle barre
larghezza_barre = 0.25

# Posizione delle barre sul grafico
posizioni2021 = np.arange(len(mesi))
posizioni2022 = [x + larghezza_barre for x in posizioni2021]
posizioni2023 = [x + 2 * larghezza_barre for x in posizioni2021]

# Creazione del grafico a barre
plt.bar(posizioni2021, valori2021, width=larghezza_barre, label='2021')
plt.bar(posizioni2022, valori2022, width=larghezza_barre, label='2022')
plt.bar(posizioni2023, valori2023, width=larghezza_barre, label='2023')

# Aggiunta di etichette agli assi e al titolo
plt.xlabel('Mesi')
plt.ylabel('Valore')
plt.title('Confronto valori mensili per anni')
plt.xticks([r + larghezza_barre for r in range(len(mesi))], mesi)
plt.legend()

# Mostra il grafico
plt.show()
