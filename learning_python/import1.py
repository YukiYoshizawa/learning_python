import tax       #手順１で作ったモジュール(ファイル名の.pyより前の部分を指定する)

print(tax.postTaxPrice(120), "円")      #関数を呼び出すときは「モジュール名.関数名」
print(tax.postTaxPrice(128), "円")
print(tax.postTaxPrice(980), "円")