def F(n):
    if n <= 2:
        return n + 1
    else:
        return F(n - 1) + 2 * F(n - 2)


print(F(4))
