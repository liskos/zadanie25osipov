def f(n):
    k = 0
    a = []
    for i in range(30, 63):
        a.append(i)
    b = []
    for i in range(25, 39):
        b.append(i)
    c = []
    for i in range(40, n+1):
        c.append(i)
    for x in range(1, 1000):
        if (x not in a or x in b) and (x in c or x in b):
            k += 1
    if k > 20:
        return True
    return False


for i in range(41, 1000):
    if f(i):
        print(i)
        break