def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y-40)<a)and((30-y)<a)or((x*y)>20)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
