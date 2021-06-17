def f(x):
    L, M = 0, 1
    while x > 0:
        L = x % 10 * M + L
        x = x // 10
        M = M * 10
    return L


for i in range(10000):
    a, k = f(i), 0
    while a > 0:
        k += a % 10
        a = a // 10
    if k == 15:
        print(i)
        break
