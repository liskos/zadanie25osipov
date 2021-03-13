def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                if not(((5*y+2*x+4*z)!=80) or (6*x >a)or (y>a)or (3*z>a)):
                    return False
    return True


for i in range(1000):
    if f(i):
        print(i)
