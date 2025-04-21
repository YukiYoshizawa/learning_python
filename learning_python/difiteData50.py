import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

for i in range(50):                             #50回繰り返す
  plt.subplot(5, 10, i + 1)                     #5x10に順番に表示する
  plt.axis("off")                               #枠線を非表示
  plt.title(digits.target[i])                   #この数字は何か
  plt.imshow(digits.images[i], cmap="Greys")    #数値データをグレーの濃淡画像にする

plt.show()                                      #画像を表示する