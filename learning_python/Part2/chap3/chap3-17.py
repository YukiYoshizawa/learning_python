import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro", "Hiragino sans", "BIZ UDGothic", "MS Gothic"]

# CSVファイルを読み込む
df = pd.read_csv("test.csv", index_col=0)

# 棒グラフを作って表示する(科目ごとの棒グラフにする)
df.T.plot.bar()           #行と列を入れ替える.Tを追加
plt.legend(loc="lower right")
plt.show()