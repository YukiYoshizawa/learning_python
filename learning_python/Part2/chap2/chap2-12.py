import requests

# 画像ファイルを取得する
image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)

# URLから最後のファイル名を取り出す
filename = image_url.split("/")[-1]
"""
保存する際にファイル名が必要なので、URLから拝借したい。URLを「/」でリスト(配列)に分割する。
リストの最後が名前に良さそうなので、リストの後ろから1番目を[-1]で指定して取り出す。
"""

# 画像データをファイルに書き出す
with open(filename, mode="wb") as f:      #バイナリー書き込みモードで開く、画像ファイなのでmode="wb"
  f.write(imgdata.content)                #画像データを書き込む
