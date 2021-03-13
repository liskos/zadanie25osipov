def f(a):
    for x in range(1, 200):
        for y in range(1, 200):
            if not(((5*y+4*x)>a) or ((2*x + 3*y)<90)or ((y - 2*x) < -150)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
