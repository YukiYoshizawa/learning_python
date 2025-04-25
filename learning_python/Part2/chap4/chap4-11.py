import pandas as pd

# CSVファイルをデータフレームに読み込む
df1 = pd.read_csv("Preview_20250425113147.csv", index_col="時点", skiprows=1)
df2 = pd.read_csv("Preview_20250425113225.csv", index_col="時点", skiprows=1)
df3 = pd.read_csv("Preview_20250425113243.csv", index_col="時点", skiprows=1) 
# skiprows=1は1行目をスキップするという命令。(ヘッダーが2行目以降にある場合の対策)
# index_col="時点"で行番号(0,1,2...)ではなく、CSVファイル内に記載がある通りに(2025年,2026年,2027年...)にインデックスを変更している。

print(df1.columns.values)
print(df2.columns.values)
print(df3.columns.values)