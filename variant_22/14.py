s = (24400 - 1) * (42200 + 2)
k = 0
while s > 0:
    k += s % 2
    s = s // 2
print(k)
