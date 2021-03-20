def f(n):
    if n == 1:
        return 1
    if n%2 == 0:
        return 2*n + f(n-1)
    return 3*f(n-2)


print(f(18))
