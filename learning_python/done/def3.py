# 引数だけある関数
def sayhello2(name):
  print("こんにちは、" + name + "さん。" )

sayhello2("田中")

# 戻り値だけある関数
import random
def omikuji():
  kuji = ['大吉', '中吉', '小吉', '凶']
  return random.choice(kuji)
kekka = omikuji()
print("結果は" , kekka, "です")