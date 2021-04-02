def f(x):
    x1 = (x // 100) + (x // 10 % 10)
    x2 = (x % 100) + (x // 10 % 10)
    if x1 > x2:
        return str(x1) + str(x2)
    return str(x2) + str(x1)


for i in range(100, 1000):
    if f(i) == '128':
        print(i)
        break
###!!!!!!!!!