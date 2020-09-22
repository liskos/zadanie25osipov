for a in range(8800, 55536):
    x = str(a)
    M = 0
    k = 0
    a1 = a // 10000
    if a1 == 0:
        a1 = 1
    a2, a3, a4, a5 = a // 1000 % 10, a // 100 % 10, a // 10 % 10, a % 10
    if '7' in x and a1 * a2 * a3 * a4 * a5 > 35:
        k += 1
        if M < a:
            M = a
print(k, M)