import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)                  #webページのデータを取得する

response.encoding = response.apparent_encoding    #文字化けしないようにする

filename = "download.txt"
with open(filename, mode="w") as f:           #ファイルを書き込みモードで開いて
  f.write(response.text)                      #インターネットから取得したデータを書き込む

