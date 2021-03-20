def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x+2*y>a)or(y<x)or(x<33)):
                return False
    return True


for i in range(10000, -10000, -1):
    if f(i):
        print(i)
        break
