def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x*x-3*x+2)>0)or(y>x*x+7)or((x*y)<a)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break