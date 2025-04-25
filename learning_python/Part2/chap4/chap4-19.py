import pandas as pd
import folium

df = pd.read_csv("200.csv", encoding="shift-jis")

hydrants = df[["緯度", "経度"]].values

# 地図にマーカーを追加して書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)   #地図の作成
for data in hydrants:
  folium.Marker([data[0], data[1]]).add_to(m)
  # リスト化した地点のデータから緯度(data[0])と経度(data[1])をマーカーとして追加する

m.save("hydrant.html")      #HTMLを保存

