import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro", "Hiragino sans", "BIZ UDGothic", "MS Gothic"]

# CSVファイルを読み込む
df = pd.read_csv("test.csv", index_col=0)

# 棒グラフを作って表示する(グラフの色を変更)
colorlist = ["skyblue", "steelblue", "tomato", "cadetblue", "orange", "sienna"]
df.T.plot.bar(color = colorlist)
plt.legend(loc="lower right")
plt.savefig("graph1.png")