def f(x):    # пробная программа для задания 23
    k = 0
    if x == 3:
        return 1
    if (x - 1) >= 3:
        k += f(x - 1)
    if (x - 2) >= 3:
        k += f(x - 2)
    if (x % 2) == 0 and (x / 2) >= 3:
        k += f(x / 2)
    return k


print(2 * f(9))
