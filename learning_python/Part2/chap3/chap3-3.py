import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)     #出力時の日本語フォントとのズレを調整

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 1列の1次元データを表示
print("国語の列の1次元データ\n",df["国語"])

# 1列の表データの表示
print("国語の列の表データ\n",df[["国語"]])

# 複数の列のデータを表示
print("国語と数学の列の表データ\n",df[["国語","数学"]])

