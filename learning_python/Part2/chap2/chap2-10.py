import requests           #復習:インターネットにアクセスを容易にする外部ライブラリ
from bs4 import BeautifulSoup     #復習:bs4内のBeautifulSoupという外部ライブラリを利用
import urllib             #相対URLを絶対URLに変換させるための外部ライブラリ

# webページを取得して解析
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 全てのaタグを検索し、リンクを絶対URLで表示する。
for element in soup.find_all("a"):          #全てのaタグを検索
  print(element.text)
  url = element.get("href")                 #href属性を取り出す
  link_url = urllib.parse.urljoin(load_url, url)    #絶対URLを取得
  print(link_url)
