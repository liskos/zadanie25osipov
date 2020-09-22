def f(x):
    a, b = 0, 1
    while x > 0:
        if x % 2 > 0:
            a += x % 8
        else:
            b *= x % 8
        x = x // 8
    return a, b


for i in range(1, 1000):
    a, b = f(i)
    if a == 2 and b == 24:
        print(i)
        break
