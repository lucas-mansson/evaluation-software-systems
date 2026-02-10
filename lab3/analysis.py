import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

df = pd.read_csv("times.csv", sep=";")

# Skapa en ny veriabel som är skillnaden mellan gissning och faktisk tid
df["skillnad"] = df["Faktisk tid"] - df["Estimerad tid"] 

#print(df)

print("Skattning av tid")
estimation_summary = df.groupby("Grupp A/B")["Estimerad tid"].agg(["mean", "std"])
print(estimation_summary)

print("T-test")
grupp_a = df[df["Grupp A/B"] == "A"]["Estimerad tid"]
grupp_b = df[df["Grupp A/B"] == "B"]["Estimerad tid"]

t_stat, p_value = st.ttest_ind(grupp_a, grupp_b)

print(f"Grupp A Medelfel: {grupp_a.mean():.2f} min (Standardavvikelse: {grupp_a.std():.2f})")
print(f"Grupp B Medelfel: {grupp_b.mean():.2f} min (Standardavvikelse: {grupp_b.std():.2f})")
print(f"T-statistik: {t_stat:.4f}")
print(f"P-värde: {p_value:.4f}")

print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")

print("Skillnader")
difference_summary = df.groupby("Grupp A/B")["skillnad"].agg(["mean", "std"])
print(difference_summary)

print("T-test")
grupp_a = df[df["Grupp A/B"] == "A"]["skillnad"]
grupp_b = df[df["Grupp A/B"] == "B"]["skillnad"]

t_stat, p_value = st.ttest_ind(grupp_a, grupp_b)

# Skapa box-plot
df.boxplot(column="skillnad", by="Grupp A/B")
plt.title("Skillnad mellan faktisk och estimerad tid")
plt.ylabel("Minuter (Skillnad)")
plt.show()
plt.savefig("difference.png")

# Skriv ut resultat
print(f"Grupp A Medelfel: {grupp_a.mean():.2f} min (Standardavvikelse: {grupp_a.std():.2f})")
print(f"Grupp B Medelfel: {grupp_b.mean():.2f} min (Standardavvikelse: {grupp_b.std():.2f})")
print(f"T-statistik: {t_stat:.4f}")
print(f"P-värde: {p_value:.4f}")
