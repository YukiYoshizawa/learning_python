import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)     #出力時の日本語フォントとのズレを調整

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 「名前」の列を削除
print("「名前」の列を削除\n", df.drop("名前", axis=1))

# インデックス2の行を削除
print("インデックス2の行を削除\n", df.drop(2, axis=0))
