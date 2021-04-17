def f(x):
    P = 90
    S = 6 * (x - x % 22)
    K = 0
    while P < 181:
        K = K + 1
        P = P + K
        S = S - 2 * K
    return S


for i in range(10000, -10000, -1):
    if f(i) == 82:
        print(i)
        break
