def f(n):
    k = 0
    a = []
    for i in range(27, 55):
        a.append(i)
    b = []
    for i in range(32, 47):
        b.append(i)
    c = []
    for i in range(n, 71):
        c.append(i)
    for x in range(1, 1000):
        if (x not in a or x in b) and (x in c or x in b):
            k += 1
    if k > 25:
        return True
    return False


for i in range(70):
    if f(i):
        print(i)
