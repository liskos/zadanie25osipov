for s in range(1, 10000):
    n = 0
    while s - n > 0:
        s -= 10
        n += 15
    if n == 165:
        print(n, s)
