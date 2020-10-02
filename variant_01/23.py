def utroitel(a, b):
    if a == b:
        return 1
    if b < a:
        return 0
    if b % 3 == 0:
        return utroitel(a, b-1) + utroitel(a, b // 3)
    return utroitel(a, b-1)


print(utroitel(3, 36))
