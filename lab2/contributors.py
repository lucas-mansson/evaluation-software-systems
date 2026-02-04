import pandas as pd
import matplotlib.pyplot as plt

def contributors(file: str, n: int):
    data = pd.read_table(file, sep="|", names=["revision", "author", "datetime", "nbr_lines"])
    data["datetime"] = pd.to_datetime(data["datetime"].str.replace(r"\+.*", "", regex=True))

    data["author"].value_counts().head(n).plot(kind='bar', x="author", y="frequency")
    plt.tight_layout()
    plt.savefig("contributors.png") # plt.show() fungerar inte i min terminal

    return data.sort_values("datetime").groupby("author").tail(1).set_index("author")["datetime"]

if __name__ == "__main__":
    print(contributors("newfile.txt", 44))
