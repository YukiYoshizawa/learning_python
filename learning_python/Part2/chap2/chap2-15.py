# ページ内画像を一括でダウンロードするプログラム

import urllib.parse
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

# webページを取得して解析する
load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 保存用フォルダを作る
out_folder = Path("download2")
out_folder.mkdir(exist_ok=True)

# 全てのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):
  src = element.get("src")

  # 絶対URLを作って、画像データを取得する
  image_url = urllib.parse.urljoin(load_url, src)
  imgdata = requests.get(image_url)

  # URLから最後のファイル名を取り出して、保存フォルダ名と繋げる
  filename = image_url.split("/")[-1]
  out_path = out_folder.joinpath(filename)

  # 画像データを、ファイルに書き出す
  with open(out_path, mode="wb") as f:
    f.write(imgdata.content)

  # 1回アクセスしたので1秒待つ
  time.sleep(1)