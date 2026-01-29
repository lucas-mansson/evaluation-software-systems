import pandas as pd

data = pd.read_csv("data.csv")

data.info()
print()
print("head():\n " + str(data.head()))
print()
print("index:\n" + str(data.index))
print()
print("columns:\n" + str(data.columns))
