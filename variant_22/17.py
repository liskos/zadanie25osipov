minch, maxch, k = 7858, 0, 0
for i in range(2476, 7858):
    if i % 2 == 0 and i % 8 != 0 and int(str(i)[-3]) < 8:
        k += 1
        minch = min(i, minch)
        maxch = max(i, maxch)
print(k, (minch + maxch) // 2)
