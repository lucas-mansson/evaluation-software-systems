import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

df["Time"] = pd.to_datetime(df["Time"], unit="s")

df = df.set_index("Time")


axes = df.plot(figsize=(12, 4), subplots=True, x_compat=True)
axes[0].set_title("a, Utomhustemtperaratur (grader C)", loc="left")
axes[1].set_title("b, Lufttryck (hPa) vid mätaren", loc="left")
axes[2].set_title("c, Luftfuktighet (%rh)", loc="left")
axes[3].set_title("d, Ljusintensitet (Lux)", loc="left")
axes[0].legend(loc=4)
axes[1].legend(loc=4)
axes[2].legend(loc=4)
axes[3].legend(loc=4)
plt.tight_layout()

plt.savefig('output.png')
