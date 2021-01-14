def f(x):
    if x < 3:
        return x
    else:
        return f(x - 1) + g(x - 2)


def g(x):
    if x < 3:
        return x + 1
    else:
        return g(x - 1) + f(x - 2)


print(f(28))
