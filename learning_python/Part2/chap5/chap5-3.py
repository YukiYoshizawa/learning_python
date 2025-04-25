import json
from pprint import pprint
# 標準ライブラリのpprint(pretty-print)を使うと綺麗に整形して表示する事ができる。

with open("test2.json", mode="r") as f:
  jsondata = json.loads(f.read())
  pprint(jsondata)

  # test2のデータは配列で格納されている。