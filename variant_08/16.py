def f(n):
    if n > 70:
        return n - 50
    else:
        return f(n + 2) + 2 * f(3 * n)


print(f(40))
