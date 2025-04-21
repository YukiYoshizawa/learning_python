"""
画像表示アプリを作成する
このアプリは、ウィンドウを表示する「tkinter」、ファイルダイアログを扱う「tkinter.filedialog」
画像を扱う「PIL.Image」、画像をtkinterで作った画面上に表示させる「PIL.ImageTk」
の4つのモジュールを使う。
"""

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image                #PIL(pillow)パッケージ全体をimportせずに、特定モジュールのみをインポートしている。
import PIL.ImageTk              #これには無駄なリソース消費を抑えたり、名前の競合回避、可読性の向上などの理由がある。

def dispPhoto(path):
  #画像を読み込んで、モザイクに変換
  newImage = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300), resample=0)
  #縮小してから拡大することでモザイク画像になる
  #そのイメージをラベルに表示する
  imageData = PIL.ImageTk.PhotoImage(newImage)
  imageLabel.configure(image = imageData)
  imageLabel.image = imageData                      #画像を300x300にリサイズして「ラベルに表示できるデータ」に変換し表示している

def openFile():                           #ファイルダイアログを開くための関数
  fpath = fd.askopenfilename()            #ファイルダイアログを開いて、選択したファイル名を取得する
  if fpath:                               #もしファイル名があったら
    dispPhoto(fpath)                      #そのファイル名で関数を呼び出す

root = tk.Tk()
root.geometry("400x350")                  #この2行で画面を作る

btn = tk.Button(text="ファイルを開く", command = openFile)           #ボタンを作って関数を指定する
imageLabel =tk.Label()                    #画面表示用のラベルを作る
btn.pack()                                #画面にボタンを配置する
imageLabel.pack()                         #画面にラベルを配置する
tk.mainloop()                             #作ったウィンドウを表示する
