# 全てのimgタグの画像ファイルURLを表示する

import requests
from bs4 import BeautifulSoup
import urllib

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 全てのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):          #全てのimgタグを取得
  src = element.get("src")                    #src属性を取得

  # 絶対URLと、ファイルを表示する
  image_url = urllib.parse.urljoin(load_url, src)     #絶対URLを取得
  filename = image_url.split("/")[-1]                 #ファイル名を取得
  print(image_url, ">>", filename)
