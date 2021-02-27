def f(n):
    k = 0
    for x in range(1, 1000):
        if not(x in [80,91] or x in [30,51]) and (x in [10, n+1] or x in [80, 91]):
            k += 1
    if k > 25:
        return True
    return False


for i in range(11, 1000):
    if f(i):
        print(i)
        break
