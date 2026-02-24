import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# run the experiment
inFile = "data1.txt"
n=600
python_n = 10
description = f"Collections.sort-{inFile}-{n}"
javaResultFile = f"{description}.csv"
pythonResultFile = f"python_averages_{python_n}.csv"

for i in range (10): 
    print(f"Starting time measurements, {description}")
    subprocess.run(["java", "Measure",  inFile, javaResultFile,  str(n)])

    #läs ut-filen med 600 tider, räkna ut medelvärde i jämviktsläget, spara medelvärdet
    df = pd.read_csv(javaResultFile, index_col=0)
    averages = df[350:].mean() # 350 insvängning
    averages.to_csv(pythonResultFile, mode='a', header=False, index=False)

# analyse the measured times
#plt.savefig(f"{javaResultFile}.png")
