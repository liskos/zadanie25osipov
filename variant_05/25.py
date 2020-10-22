def delit(x):
    chyot, nechyot = 0, 0
    minimal = x
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            if i % 2 == 0 and x // i % 2 == 0:
                chyot += 2
            elif i % 2 == 1 and x // i % 2 == 1:
                nechyot += 2
            else:
                chyot += 1
                nechyot += 1
        if minimal > i and i > 1000:
            minimal = i
    return chyot, nechyot, minimal


for i in range(326496, 649633):
    a, b, m = delit(i)
    if a > 70 and a == b:
        print(i, m)
