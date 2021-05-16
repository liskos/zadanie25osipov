def f(s):
    n = 1
    while s < 47:
        s = s + 4
        n = n * 2
    return n


for i in range(10000, 0, -1):
    if f(i) == 64:
        print(i)
        break
