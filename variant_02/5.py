def d30(N):
    x1 = str(N // 100)
    x2 = str((N // 10) % 10)
    x3 = str(N % 10)
    if x1 >= x2 and x1 >= x3:
        M = x1
        if x2 > x3:
            M += x2
            m = x3 + x2
        else:
            M += x3
            m = x2 + x3
    elif x2 >= x1 and x2 >= x3:
        M = x2
        if x1 > x3:
            M += x1
            m = x3 + x1
        else:
            M += x3
            m = x1 + x3
    else:
        M = x3
        if x2 > x1:
            M += x2
            m = x1 + x2
        else:
            M += x1
            m = x2 + x1
    R = int(M) - int(m)
    return R


k = 0
for a in range(800,901):
    if d30(a) == 30:
        k += 1
print(k)