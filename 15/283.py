def f(n):
    k = 0
    a = list(range(80, 91))
    b = list(range(30, 51))

    for x in range(1, 1000):
        c = [i for i in range(10, n + 1)]
        if (x in a or x in b) and (x in c or x in a):
            k += 1
    if k > 25:
        return True
    return False


for i in range(1, 1000):
    if f(i):
        print(i)
        break
