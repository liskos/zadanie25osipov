def f(x):
    a, b = 0, 1
    while x > 0:
        if x % 2 > 0:
            a += 1
        else:
            b += x % 5
        x = x // 5
    return a, b


for i in range(1000):
    a, b = f(i)
    if a == 2 and b == 9:
        print(i)
        break
