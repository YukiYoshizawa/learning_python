import pandas as pd

# CSVファイルをデータフレームに読み込む
# df = pd.read_csv("FEH_00200524_250424180827.csv", index_col="全国・都道府県", encoding="utf-8")
with open("FEH_00200524_250424180827.csv", "r", encoding="utf-8", errors="replace") as f:
    df = pd.read_csv(f, index_col="全国・都道府県")

print(len(df))
print(df.columns.values)