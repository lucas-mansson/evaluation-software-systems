import pandas as pd

from remove_na import remove_na
from analyze_outliers import analyze_potential_outliers

data = pd.read_csv("data.csv")
data = remove_na(data)

outliers = analyze_potential_outliers(data=data, threshold=[1, 2, 3])

print(outliers)
