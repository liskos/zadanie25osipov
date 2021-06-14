def f(a, b):
    if a > b:
        return 0
    if a == b:
        return  1
    return f(a + 1, b) + f(a + 2, b) + f(a * 2, b)


print(f(4, 10) * f(10, 12) * f(12, 14))
