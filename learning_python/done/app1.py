import tkinter as tk          #ティーケーインター

def dispLabel():
  lbl.configure(text="こんにちは")  #ラベルの文字を「こんにちはに変更する」

root = tk.Tk()                #画面を作る
root.geometry("200x100")      #画面の大きさを決める(xは半角英字の小文字のエックス)

lbl = tk.Label(text="LABEL")  #ラベルを作る
btn = tk.Button(text="PUSH", command = dispLabel)  #ボタンを作る、ボタンで関数を実行するように修正する

lbl.pack()                    #画面にラベルを配置する
btn.pack()                    #画面にボタンを配置する
tk.mainloop()                 #作ったウィンドウを表示する