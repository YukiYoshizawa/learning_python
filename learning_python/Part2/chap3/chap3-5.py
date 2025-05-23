import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)     #出力時の日本語フォントとのズレを調整

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 1列のデータを追加
df["美術"] = [68, 73, 82, 77, 94, 96]
print("列データ(美術)を追加\n",df)

# 1行データを追加
df.loc[6] = ["G恵", 90, 92, 94, 96, 92, 98]
print("行データ(G恵)を追加\n", df)
