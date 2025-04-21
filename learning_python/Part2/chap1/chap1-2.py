import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)                  #webページのデータを取得する

response.encoding = response.apparent_encoding    #文字化けしないようにする

filename = "download.txt"
f = open(filename, mode="w")                #ファイルを書き込みモードで開く

f.write(response.text)                       #インターネットから取得したデータを書き込む

f.close                                     #ファイルを閉じる

