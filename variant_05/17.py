a = []
for i in range(100001, 900010):
    if (i % 7 + i % 10) == 10 and i % 11 == 0 and i % 55 != 0:
        a.append(i)
print(max(a), len(a))
