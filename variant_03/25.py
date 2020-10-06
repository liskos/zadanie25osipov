a = []
for i in range(1024, 28922):
    c = str(i)
    if i < 10000:
        x1, x2, x3, x4 = map(int, c)
        x5 = 0
    else:
        x1, x2, x3, x4, x5 = map(int, c)
    if i % x1 + x2 + x3 + x4 + x5 == 0:
        a.append(i)
print(sum(a))
