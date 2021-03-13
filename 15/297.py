def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((3*y+x)<a) or (3*x + 2*y>80)or (3*x - 4*y > 90)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break