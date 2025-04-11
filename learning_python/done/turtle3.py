from turtle import *
shape("turtle")
col = ["orange", "limegreen","gold", "plum","tomato"]   #色の名前を5つ準備
for i in range(5):                                      #以下の3行を5回繰り返す
  color(col[i])                                         #線の色を変える
  forward(200)                                          #まっすぐ200進む
  left(144)                                             #左に144度曲がる
done()