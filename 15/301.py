def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((5*y-x)>a) or ((2*x + 3*y)<90)or ((y - 2*x) < -50)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
