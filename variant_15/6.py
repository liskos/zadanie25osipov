def f(d):
    n = 20
    s = 40
    while s + n < d:
        s = s - 10
        n = n - 20
    return n


for i in range(1, 10000):
    if f(i) >0:
        print(i)
