import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

df = pd.read_csv("times.csv", sep=";")

# Skapa en ny veriabel som är skillnaden mellan gissning och faktisk tid
df["skillnad"] = df["Faktisk tid"] - df["Estimerad tid"] 

print(df)

print("sammanfattning skillnader")
stats_summary = df.groupby('Grupp A/B')['skillnad'].agg(['mean', 'std', 'count'])
print(stats_summary)

print("T-test")
grupp_a = df[df['Grupp A/B'] == 'A']['skillnad']
grupp_b = df[df['Grupp A/B'] == 'B']['skillnad']


t_stat, p_value = st.ttest_ind(grupp_a, grupp_b)

# Skapa box-plot
plt.figure(figsize=(7, 5))
df.boxplot(column='skillnad', by='Grupp A/B')
plt.title('Skillnad mellan faktisk och estimerad tid')
plt.suptitle('') # Ta bort pandas standard-titel
plt.ylabel('Minuter (Faktisk - Estimerad)')
plt.axhline(y=0, color='r', linestyle='--') # Noll-linje (perfekt estimering)
plt.show()

# Skriv ut resultat
print(f"Grupp A Medelfel: {grupp_a.mean():.2f} min (Standardavvikelse: {grupp_a.std():.2f})")
print(f"Grupp B Medelfel: {grupp_b.mean():.2f} min (Standardavvikelse: {grupp_b.std():.2f})")
print(f"T-statistik: {t_stat:.4f}")
print(f"P-värde: {p_value:.4f}")
