def f(x):
    s, n = 0, 0
    while s < 111:
        s += 8
        n += x
    return n


for i in range(1000):
    print(f(i), i)
    if f(i) == 28:
        break
