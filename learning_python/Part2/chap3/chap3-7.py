import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)     #出力時の日本語フォントとのズレを調整

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 条件に合うデータを抽出する
data_s = df[df["国語"]>= 90]
print("国語が90点以上\n", data_s)

data_c = df[df["数学"]<70]
print("数学が70点未満\n", data_c)
