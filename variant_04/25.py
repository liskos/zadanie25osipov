def delitely(x):
    k = 0
    a = []
    for i in range(10, 100):
        if x % i == 0:
            a.append(i)
            k += 1
    return k, a


for i in range(333555, 778000):
    k, a = delitely(i)
    if k == 35:
        print(min(a), max(a))
    a = 0
