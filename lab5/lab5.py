import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# run the experiment
inFile = "data1.txt"
n=600
description = f"Collections.sort-{inFile}-{n}"
resultFile = f"{description}.csv"

print(f"Starting time measurements, {description}")
subprocess.run(["java", "Measure",  inFile, resultFile,  str(n)])

# analyse the measured times
df = pd.read_csv(resultFile, index_col=0)
df.plot()
plt.show()
print(df)
