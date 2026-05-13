import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Завантаження даних "Млин"
df = pd.read_csv('Final_Report_Mlyn.csv')

# Відфільтровуємо лише надійні дані для графіків
df_reliable = df[df['Status'] == 'Reliable'].copy()

# --- ГРАФІК 1: ОСНОВНИЙ СКЛАД (PHYLUM) ---
plt.figure(figsize=(14, 8))
data = df_reliable['Phylum'].value_counts(normalize=True) * 100

# Групуємо все, що менше 2%, в "Others"
threshold = 2.0
main_sectors = data[data >= threshold].copy()
others = data[data < threshold].sum()
if others > 0:
    main_sectors['Others'] = others

# Налаштування кольорів та "вибуху" секторів
colors = plt.cm.tab20(np.linspace(0, 1, len(main_sectors)))
explode = [0.05] * len(main_sectors)

wedges, texts, autotexts = plt.pie(
    main_sectors, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode, 
    pctdistance=0.85
)

plt.setp(autotexts, size=10, weight="bold")
plt.legend(wedges, main_sectors.index, title="Phylum Groups", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Taxonomic Composition: Mlyn Station (Main Groups)', fontsize=16, weight='bold')
plt.tight_layout()
plt.savefig('main_composition.png') # Зберігаємо для GitHub
plt.show()

# --- ГРАФІК 2: ДЕТАЛІЗАЦІЯ РІДКІСНИХ ВИДІВ ---
plt.figure(figsize=(12, 8))
minority = data[data < threshold].sort_values()

if not minority.empty:
    minority.plot(kind='barh', color='salmon')
    plt.title('Detailed View: Rare Phyla (<2%)', fontsize=14)
    plt.xlabel('Percentage in Sample (%)')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('minority_details.png') # Зберігаємо для GitHub
    plt.show()
else:
    print("Рідкісних груп менше 2% не знайдено.")
