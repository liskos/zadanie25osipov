s = 8 ** 1023 + 2 ** 1024 - 3
k = 0
while s > 0:
    k += s % 2
    s = s // 2
print(k)
