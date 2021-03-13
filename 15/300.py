def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y-x)>a) or ((x + 4*y)>40)or ((y - 2*x) < -35)):
                return False
    return True


for i in range(-1000,1000):
    if f(i):
        print(i)
