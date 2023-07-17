import matplotlib.pyplot as plt
import locale

# Imposta il separatore delle migliaia
locale.setlocale(locale.LC_ALL, '')

# Dati
mesi = ['Gen', 'Feb', 'Mar', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']

valori2023 = [150000, 250000, 300000, 550000, 45000, 150000, 50000, 650000, 95000, 1000000, 120000]
valori2022 = [50000, 20000, 30000, 50000, 45000, 10000, 350000, 65000, 9500, 10000, 12000]
valori2021 = [15000, 25000, 35000, 25000, 45000, 15000, 5000, 6500, 9500, 10000, 12000]

# Calcolo dei valori totali per anno
totale2023 = sum(valori2023)
totale2022 = sum(valori2022)
totale2021 = sum(valori2021)

# Creazione delle aree colorate
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Area 2021
axs[0].fill_between(mesi, valori2021, color='green', alpha=0.4)
axs[0].text(0.5, 0.5, f'{locale.format_string("%d", totale2021, grouping=True)}€', color='royalblue', horizontalalignment='center', verticalalignment='center', fontsize=16, weight='bold')
axs[0].set_title('2021')
axs[0].set_xlabel('Mesi')
axs[0].set_ylabel('Valore')

# Area 2022
axs[1].fill_between(mesi, valori2022, color='blue', alpha=0.4)
axs[1].text(0.5, 0.5, f'{locale.format_string("%d", totale2022, grouping=True)}€', color='royalblue', horizontalalignment='center', verticalalignment='center', fontsize=16, weight='bold')
axs[1].set_title('2022')
axs[1].set_xlabel('Mesi')
axs[1].set_ylabel('Valore')

# Area 2023
axs[2].fill_between(mesi, valori2023, color='orange', alpha=0.4)
axs[2].text(0.5, 0.5, f'{locale.format_string("%d", totale2023, grouping=True)}€', color='royalblue', horizontalalignment='center', verticalalignment='center', fontsize=16, weight='bold')
axs[2].set_title('2023')
axs[2].set_xlabel('Mesi')
axs[2].set_ylabel('Valore')

# Ridimensiona le aree per evitare sovrapposizioni
plt.tight_layout()

# Mostra il grafico
plt.show()
