import numpy as np
import pandas as pd
import scipy.stats as stats

def confidenceInterval(data, confidence=0.95):
  mean = np.mean(data)
  std_err = stats.sem(data)  # Standard error of the mean
  return stats.t.interval(confidence=confidence, df=len(data)-1, loc=mean, scale=std_err)

data = pd.read_csv("times.csv", sep=";")

data = pd.to_numeric(data[""])

print(f"95% Confidence Interval: {confidenceInterval(data)}")
