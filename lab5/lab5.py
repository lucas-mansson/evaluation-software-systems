from csv import Error
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import sys

if(len(sys.argv) != 4):
    raise Error("Usage: python lab5.py: [python_n] [algoritm] [jit]")

python_n = int(sys.argv[1]) # antal körningar i python, 10 eller 100
algoritm = sys.argv[2]
jit = sys.argv[3]

if(python_n not in [10, 100]):
    raise Error("python_n must be 10 or 100")

if(algoritm not in["collections", "own"]):
    raise Error("algoritm must be 'collections' or 'own'")

if(jit not in ["jit", "no_jit"]):
    raise Error("jit must be 'jit' or 'no-jit'")

# run the experiment
inFile = "data1.txt"
n=600
java_results = f"{algoritm}.sort-{inFile}-{n}.csv"
python_averages = f"averages_{python_n}_{algoritm}_{jit}.csv"

averages = []
for i in range(python_n): 
    percent = int((i/(python_n-1))*100)
    print(f"\r[{"█" * percent}{" " * (100-percent-1)}] {percent}%" , end="", flush=True)

    subprocess.run(["java", "Measure",  inFile, java_results,  str(n), algoritm ])

    #läs ut-filen med 600 tider, räkna ut medelvärde i jämviktsläget, spara medelvärdet
    df = pd.read_csv(java_results)
    averages.append(df["time"][350:].mean()) # 350 insvängning

print("\n")

# Konvertera till numpy array sen series för att skriva till csv
pd.Series(np.array(averages)).to_csv(python_averages, index=False)

# räkna ut medelvärde och konfidensintervall för de 10/100 sparade medelvärdena
data = pd.read_csv(python_averages)
mean = data.mean()
std_err = stats.sem(data)  # Standard error of the mean
print(f"konfidensintervall: { stats.t.interval(confidence=0.95, df=len(data)-1, loc=mean, scale=std_err)}")
print(f"mean: {mean}")

