import requests
from bs4 import BeautifulSoup

load_url = "https://www.aozora.gr.jp/cards/000879/files/92_14545.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")


# 要素 = soup.find("タグ名", class_="class名")で取り出す事ができる
# フリガナのrbタグは無視されるので本文のみが抽出される。
title = soup.find("h1", class_="title")
print("タイトル：", title.text)
author = soup.find("h2", class_="author")
print("作者", author.text)
content = soup.find("div", class_="main_text")
print("本文", content.text)