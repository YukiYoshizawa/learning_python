total = 0

for i in range(10):
  for j in range(10):
    print(j, "x", i, "=", j*i)
    total = total + j*i

print(total)