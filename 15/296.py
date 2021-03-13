def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((2*y+5*x)<a) or (2*x + 4*y>100)or (3*x - 2*y > 70)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break