def f(d):
    n = 5
    s = 83
    while s <= 1200:
        s = s + d
        n = n + 6
    return n

a = []
for i in range(1, 1000):
    k = f(i)
    if k == 89:
        a.append(i)
print(max(a))
