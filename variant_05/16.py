def f(x):
    if x < 5:
        return 5 - x
    elif x % 3 == 0:
        return 4 * (x - 5) * f(x-5)
    else:
        return 3 * x + 2 * f(x - 1) + f(x - 2)


print(f(20))
