def f(a):
    for x in range(1000):
        if not(not (x&a) or not(x&36==0) or (x&6)):
            return False
    return True


for i in range(10000, -10000, -1):
    if f(i):
        print(i)
        break
