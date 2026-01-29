import pandas as pd

def remove_na(df: pd.DataFrame):
    return df.dropna()

if __name__ == "__main__":

    df = pd.DataFrame({
      "a": [12, pd.NA, 10, pd.NA],
      "b": [11, pd.NA, 15, 20]
    })

    print("Before")

    df.info()
    print()
    print("head():\n " + str(df.head()))
    print()
    print("index:\n" + str(df.index))
    print()
    print("columns:\n" + str(df.columns))

    df = remove_na(df)

    print("after")
    df.info()
    print()
    print("head():\n " + str(df.head()))
    print()
    print("index:\n" + str(df.index))
    print()
    print("columns:\n" + str(df.columns))
