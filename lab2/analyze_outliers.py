import pandas as pd

def analyze_potential_outliers(data: pd.DataFrame, threshold: list[float]): 
    nbr_outliers = (data > threshold).sum()
    mean_val_outliers = data[data < threshold].mean()

    return pd.DataFrame({"nbr_outliers": nbr_outliers, "mean_val_outliers": mean_val_outliers})
