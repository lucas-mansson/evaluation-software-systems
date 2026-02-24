import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# run the experiment
inFile = "data1.txt"
n=600
python_n = 10
java_results = f"Collections.sort-{inFile}-{n}.csv"
python_averages = f"python_averages_{python_n}.csv"

averages = []
for i in range(python_n): 
    percent = int((i/(python_n-1))*100)
    print(f"\r[{"█" * percent}{" " * (100-percent-1)}] {percent}%" , end="", flush=True)

    subprocess.run(["java", "Measure",  inFile, java_results,  str(n)])

    #läs ut-filen med 600 tider, räkna ut medelvärde i jämviktsläget, spara medelvärdet
    df = pd.read_csv(java_results)
    averages.append(df["time"][350:].mean()) # 350 insvängning

print("\n")
pd.Series(np.array(averages)).to_csv(python_averages, index=False)
python_averages = f"python_averages_{python_n}_no_jit.csv"

averages = []
for i in range(python_n): 
    percent = int((i/(python_n-1))*100)
    print(f"\r[{"█" * percent}{" " * (100-percent-1)}] {percent}%" , end="", flush=True)

    subprocess.run(["java","-Xint", "Measure",  inFile, java_results,  str(n)])

    #läs ut-filen med 600 tider, räkna ut medelvärde i jämviktsläget, spara medelvärdet
    df = pd.read_csv(java_results)
    averages.append(df["time"][350:].mean()) # 350 insvängning

print("\n")
pd.Series(np.array(averages)).to_csv(python_averages, index=False)


python_n = 100
python_averages = f"python_averages_{python_n}.csv"

averages = []
for i in range(python_n): 
    percent = int((i/(python_n-1))*100)
    print(f"\r[{"█" * percent}{" " * (100-percent-1)}] {percent}%" , end="", flush=True)

    subprocess.run(["java", "Measure",  inFile, java_results,  str(n)])

    #läs ut-filen med 600 tider, räkna ut medelvärde i jämviktsläget, spara medelvärdet
    df = pd.read_csv(java_results)
    averages.append(df["time"][350:].mean()) # 350 insvängning

print("\n")

# Konvertera till numpy array sen series för att skriva till csv
pd.Series(np.array(averages)).to_csv(python_averages, index=False)

python_averages = f"python_averages_{python_n}_no_jit.csv"

averages = []
for i in range(python_n): 
    percent = int((i/(python_n-1))*100)
    print(f"\r[{"█" * percent}{" " * (100-percent-1)}] {percent}%" , end="", flush=True)

    subprocess.run(["java","-Xint", "Measure",  inFile, java_results,  str(n)])

    #läs ut-filen med 600 tider, räkna ut medelvärde i jämviktsläget, spara medelvärdet
    df = pd.read_csv(java_results)
    averages.append(df["time"][350:].mean()) # 350 insvängning

print("\n")
pd.Series(np.array(averages)).to_csv(python_averages, index=False)

