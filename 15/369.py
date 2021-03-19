def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x*x-11*x+28)>0)or((y*y-9*y+14)>0)or((x*x+y*y)>a)):
                return False
    return True


for i in range(10000, 1, -1):
    if f(i):
        print(i)
        break
