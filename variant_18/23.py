def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(2*a, b) + f(a*a, b)


print(f(5, 154))