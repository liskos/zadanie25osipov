def func(x):
    a = 0
    b = 1
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 5
        x = x // 5
    return a, b


for x in range(0, 1000000):
    a, b = func(x)
    if a == 2 and b == 9:
        print(x)
        break