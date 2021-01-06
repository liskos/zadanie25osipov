def f(x):
    if x <= 3:
        return 2 * x - 1
    else:
        return 3 * f(x - 1) + 7


print(f(15))
