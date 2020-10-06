def F(n):
    if n > 3:
        return F(n-1) + 5 * F(n - 2)
    else:
        return 2 * n + 3


print(F(10))
