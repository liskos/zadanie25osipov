def f(n):
    k = 0
    a = []
    for i in range(30, 51):
        a.append(i)
    b = []
    for i in range(40, 47):
        b.append(i)
    c = []
    for i in range(n, 62):
        c.append(i)
    for x in range(1, 1000):
        if (x in b or x not in a) and (x in c or x in b):
            k += 1
    if k > 25:
        return True
    return False


for i in range(1, 62):
    if f(i):
        print(i)
