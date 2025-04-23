import requests           #復習:インターネットにアクセスを容易にする外部ライブラリ
from bs4 import BeautifulSoup     #復習:bs4内のBeautifulSoupという外部ライブラリを利用

# webページを取得して解析
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 全てのaタグを検索して、リンクを表示する
for element in soup.find_all("a"):          #全てのaタグを検索
  print(element.text)
  url = element.get("href")                 #href属性を取り出す
  print(url)

"""
実行結果は
リンク1
https://www.ymori.com/books/python2nen/test1.html
リンク2
./test3.html
になる。2つ目のリンクは相対URLになっているのでこれを絶対URLに変換する必要がある。
urllibライブラリを使うことで変換する事ができる。2-10へ
"""