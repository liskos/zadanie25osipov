def f(x):
    S = 1
    A = 11
    while x // 7 > 0:
        if x % 7 < 4:
            S = S + A
        else:
            S = S + (x % 7)
        x = x // 7
    return S


a = []
for i in range(1, 100000):
    if f(i) > 25:
        a.append(f(i))
print(min(a))
b = []
minn = min(a)
for i in range(1, 100000):
    if f(i) == minn:
        b.append(i)
print(min(b))
