def f(x):
    S = 0
    while x > 0:
        if x % 2 > 0:
            S = S + (x % 7)
        else:
            S = S - (x % 7)
        x = x // 7
    return S


for i in range(51, 10000):
    if f(i) == 1:
        print(i)
        break