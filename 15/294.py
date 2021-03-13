def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y+4*x)<a) or (x + 3*y>100)or (5*x + 2*y > 150)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break