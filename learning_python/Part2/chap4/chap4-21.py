import pandas as pd

df=pd.read_csv("898.csv")

# 店舗のある地点(緯度経度)と店舗名をリスト化する
store = df[["緯度", "経度", "店舗名(日本語)"]].values
print(len(store))
print(store)

