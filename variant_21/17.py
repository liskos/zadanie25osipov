m = 0
k = 0
for i in range(4563, 7913):
    if i % 7 == 0 and (i // 1000 + i % 10) > 10:
        k += 1
        m = i
print(m, k)
