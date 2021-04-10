def f(a, b):
    if a == 15 or a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(2*a, b)


print(f(1, 10)*f(10, 21))
