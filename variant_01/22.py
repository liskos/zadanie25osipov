def st(x):
    a, b = 0, 1
    while x > 0:
        a += 1
        b = b * (x % 10)
        x = x // 10
    return a, b


for x in range(1, 1000):
    a, b = st(x)
    if a == 3 and b == 12:
        print(x)
        break