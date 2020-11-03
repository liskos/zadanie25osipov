def f(n):
    if n > 2:
        return f(n - 2) + 2 * f(n - 1) + 7
    else:
        return 3 * n - 3


print(f(20))
