import folium

# 地図にマーカーを追加して書き出す
m = folium.Map(location=[35.942957, 136.198863], zoom_start=16)   #地図の作成
folium.Marker([35.942957, 136.198863]).add_to(m)

m.save("sabae.html")      #HTMLを保存

