def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x-20)<a)and((20-x)<a)or((x*y)>50)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
