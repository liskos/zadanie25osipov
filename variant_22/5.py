def f(n):
    r, s = n, 0
    while n > 0:
        s += n % 2
        n = n // 2
    return r * 4 + s * 2


for i in range(1, 100000):
    if f(i) > 125:
        print(i)
        break
