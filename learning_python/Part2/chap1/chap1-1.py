import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)                  #webページのデータを取得する

response.encoding = response.apparent_encoding    #文字化けしないようにする

print(response.text)                            #取得した文字列データを表示する