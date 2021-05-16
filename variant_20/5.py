def f(x):
    n = x
    s = 0
    while x > 0:
        s += x%2
        x = x // 2
    if s % 2 == 1:
        return n * 4 + 2
    else:
        return n * 4


for i in range(10000):
    r = f(i)
    if r > 396:
        print(r)
        break
