import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)     #出力時の日本語フォントとのズレを調整

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 行と列を入れ替える
print("行と列を入れ替える\n", df.T)

# データをリスト化する
print("Pythonのリストデータ化\n", df.values)

