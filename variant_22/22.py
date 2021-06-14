def f(x):
    a = 1
    b = 0
    while x > 0:
        b = b + 1
        if x % 2 == 0:
            a = a * (x % 8)
        x = x // 8
    return a, b


for i in range(100000, 1, -1):
    a, b = f(i)
    if a == 2 and b == 3:
        print(i)
        break
