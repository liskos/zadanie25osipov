def f(x):
    L = x
    M = 65
    if L % 2 == 0:
        M = 52
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M


for i in range(101, 1000000):
    if f(i) == 26:
        print(i)
        break