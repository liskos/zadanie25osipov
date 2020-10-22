def delit(x):
    chyot, nechyot = 0, 0
    minimal = x
    for i in range(2, x):
        if x % i == 0:
            if i % 2 == 0:
                chyot += 1
            else:
                nechyot += 1
        if minimal > i and i > 1000:
            minimal = i
    return chyot, nechyot, minimal


for i in range(326496, 649633):
    a, b, m = delit(i)
    if a > 70 and a == b:
        print(i, m)
#программа слишком долго работает - поэтому ответа - нет.
