"""
最高気温と最低気温のグラフも重ねて表示する。複数のグラフを表示させるので区別ができるように凡例も表示させる。
最高気温と最低気温の元のデータは列名が「東京都」になっていて区別がつかなくなるので、rename命令で列名を"東京都"
から"最高気温"、”最低気温”に変更してグラフを作成する。
グラフを重ねて表示するには、それぞれのグラフをplot()で作成して、最後にplt.show()を実行する。
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Hiragino Maru Gothic Pro", "Hiragino sans", "BIZ UDGothic", "MS Gothic"]

# CSVファイルをデータフレームに読み込む
df1 = pd.read_csv("Preview_20250425113147.csv", index_col="時点", skiprows=1)
df2 = pd.read_csv("Preview_20250425113225.csv", index_col="時点", skiprows=1)
df3 = pd.read_csv("Preview_20250425113243.csv", index_col="時点", skiprows=1) 

# 列名の変更
df2 = df2.rename(columns={"東京都":"最高気温"})
df3 = df3.rename(columns={"東京都":"最低気温"})

# 3つのグラフを重ねて表示
df1["年平均気温【℃】"].plot()
df2["最高気温"].plot()
df3["最低気温"].plot()
plt.ylim(-18,40)        #縦軸の設定
plt.legend(loc="lower right")     #凡例の表示
plt.show()

