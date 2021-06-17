s = 5 * 36 ** 7 + 6 ** 10 - 36
k = 0
while s > 0:
    if s % 6 == 5:
        k += 1
    s = s // 6
print(k)
