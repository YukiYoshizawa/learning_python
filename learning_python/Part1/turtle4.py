from turtle import *
shape("turtle")
col = ["orange", "limegreen", "gold", "plum", "tomato"]
for i in range(5):
  color(col[i])
  circle(100)         #半径100の円を描く
  left(72)            #左に72度曲がる
done()