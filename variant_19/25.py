def delit(x):
    k = 0
    a1, a2 = 0, 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            if i == x // i:
                return 0, 0
            else:
                k += 2
                a1 = i
                a2 = x // i
        if k > 2:
            return 0, 0
    return a1, a2


for i in range(174457, 174506):
    a1, a2 = delit(i)
    if a1 != 0:
        print(a1, a2)
