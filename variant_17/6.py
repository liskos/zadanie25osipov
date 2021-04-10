def f(d):
    n = 8
    s = 6
    while s <= 1800:
        s = s + d
        n = n + 7
    return n


k = 0
for i in range(1, 10000):
    if f(i) == 246:
        k += 1
print(k)
