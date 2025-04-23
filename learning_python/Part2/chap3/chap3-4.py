import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)     #出力時の日本語フォントとのズレを調整

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 1行の1次元データを表示
print("C子の行の1次元データ\n",df.loc[2])

# 1行の表データを表示
print("C子の表データ\n",df.loc[[2]])

# 複数行のデータを表示
print("C子とD郎の列の表データ\n",df.loc[[2,3]])

# 指定した行の指定した列のデータを表示
print("C子の国語データ\n", df.loc[2]["国語"])

