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


i = 0
while f(i) < 25:
    i += 1
print(i)
