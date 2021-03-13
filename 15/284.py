def f(n):
    k = 0
    a = []
    for i in range(60, 91):
        a.append(i)
    b = []
    for i in range(30, 51):
        b.append(i)
    c = []
    for i in range(35, n + 1):
        c.append(i)
    for x in range(1, 1000):
        if not(x in a or x in b) and (x in c or x in a):
            k += 1
    if k > 35:
        return True
    return False


for i in range(36, 1000):
    if f(i):
        print(i)
        break
