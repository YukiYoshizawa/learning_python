import pandas as pd

# CSVファイルをデータフレームに読み込む
df = pd.read_csv("13TOKYO.CSV", header=None, encoding="shift_jis", dtype=str)

# 「8」の列が「四谷」の住所を抽出して表示
results = df[df[8] == "四谷"]
print(results[[2,6,7,8]])
# df[df[8] == "四谷"]で検索すると完全一致したもののみが表示される

# 「8」の列に「四谷」が含まれる住所を抽出して表示
results = df[df[8].str.contains("四谷")]
print(results[[2,6,7,8]])
# df[df[8].str.contains("四谷")]で検索すると部分一致したものも含まれて表示される
