def st(s):
    n = 1
    while s < 60:
        s += 5
        n *= 3
    return n


for s in range (1, 10000):
    if st(s) == 81:
        print(s, st(s))