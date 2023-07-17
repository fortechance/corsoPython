import matplotlib.pyplot as plt
import numpy as np

# Dati
mesi = ['Gen', 'Feb', 'Mar', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']

valori2023 = [150000, 250000, 300000, 550000, 45000, 150000, 50000, 650000, 95000, 1000000, 120000]
valori2022 = [50000, 20000, 30000, 50000, 45000, 10000, 350000, 65000, 9500, 10000, 12000]
valori2021 = [15000, 25000, 35000, 25000, 45000, 15000, 5000, 6500, 9500, 10000, 12000]

# Creazione del dashboard
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Grafico a linee
axs[0, 0].plot(mesi, valori2021, marker='o', label='2021')
axs[0, 0].plot(mesi, valori2022, marker='o', label='2022')
axs[0, 0].plot(mesi, valori2023, marker='o', label='2023')
axs[0, 0].set_title('Confronto valori mensili per anni')
axs[0, 0].set_xlabel('Mesi')
axs[0, 0].set_ylabel('Valore')
axs[0, 0].legend()

# Grafico a barre
larghezza_barre = 0.3
posizioni2021 = np.arange(len(mesi))
posizioni2022 = [x + larghezza_barre for x in posizioni2021]
posizioni2023 = [x + 2 * larghezza_barre for x in posizioni2021]
axs[0, 1].bar(posizioni2021, valori2021, width=larghezza_barre, label='2021')
axs[0, 1].bar(posizioni2022, valori2022, width=larghezza_barre, label='2022')
axs[0, 1].bar(posizioni2023, valori2023, width=larghezza_barre, label='2023')
axs[0, 1].set_title('Confronto valori mensili per anni')
axs[0, 1].set_xlabel('Mesi')
axs[0, 1].set_ylabel('Valore')
axs[0, 1].set_xticks([r + larghezza_barre for r in range(len(mesi))])
axs[0, 1].set_xticklabels(mesi)
axs[0, 1].legend()

# Grafico a torta
totale2023 = sum(valori2023)
percentuali2023 = [(valore / totale2023) * 100 for valore in valori2023]
axs[1, 0].pie(percentuali2023, labels=mesi, autopct='%1.1f%%')
axs[1, 0].set_title('Distribuzione valori mensili per anno (2023)')

# Grafico a forma di tachimetro
valore_massimo = max(max(valori2021), max(valori2022), max(valori2023))
range_valori = np.linspace(0, valore_massimo, num=6)
intervalli = [range_valori[i:i+2] for i in range(len(range_valori) - 1)]
valore_tachimetro = valori2023[-1]  # Utilizza l'ultimo valore dell'anno 2023 come valore del tachimetro
colori = ['green', 'yellow', 'orange', 'red']
valori_colori = [intervalli[i][1] for i in range(len(intervalli)) if intervalli[i][1] >= valore_tachimetro]
valori_colori.append(valore_tachimetro)
colori = colori[:len(valori_colori)]
axs[1, 1].pie(valori_colori, colors=colori, wedgeprops={'width': 0.4})
axs[1, 1].set_title('Tachimetro (2023)')

# Ridimensiona i grafici per evitare sovrapposizioni
plt.tight_layout()

# Mostra il dashboard
plt.show()
