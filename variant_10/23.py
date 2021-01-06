def f(x):
    a = 0
    if x == 3:
        return 1
    if x - 1 >= 3:
        a += f(x - 1)
    if x - 2 >= 3:
        a += f(x - 2)
    if (x % 3 == 0) and (x // 3 >= 3):
        a += f(x // 3)
    return a


print(f(9))
