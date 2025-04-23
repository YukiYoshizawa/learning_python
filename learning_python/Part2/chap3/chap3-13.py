import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)     #出力時の日本語フォントとのズレを調整

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# ソート(国語の点数が高いもの順)
kokugo = df.sort_values("国語", ascending=False)

# CSVファイルに出力する
kokugo.to_csv("export3.csv", index=False, header=False)
