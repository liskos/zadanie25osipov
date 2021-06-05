def f(x):
    L = x - 16
    M = x + 16
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    return M


for i in range(101, 100000):
    if f(i) == 16:
        print(i)
        break
