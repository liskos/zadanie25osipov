def f(n):
    if n < - 100000:
        return 1
    if n > 10:
        return f(n - 1) + 3 * f(n - 3) + 2
    return -f(n - 1)


print(f(20))
#ne rabotaet