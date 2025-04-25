import json
from pprint import pprint
# 標準ライブラリのpprint(pretty-print)を使うと綺麗に整形して表示する事ができる。

with open("test2.json", mode="r") as f:
  jsondata = json.loads(f.read())
  # test2のデータは配列で格納されている。
  print("1つ目のオブジェクト = ",jsondata[0])
  print("都市名 = ", jsondata[0]["name"])
  print("緯度 = ", jsondata[0]["coord"]["lat"])
  print("経度 = ", jsondata[0]["coord"]["lon"])
  # インデックス0のcoordのlonを取得する 


  