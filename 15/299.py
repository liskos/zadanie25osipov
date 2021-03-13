def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y-x)<a) or (7*x + 4*y>350)or (3*y - 2*x > 45)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break