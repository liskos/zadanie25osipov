def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                if not(((3*y+x+2*z-54)!=0) or ((x +10)>a)or ((5*y-4*x)>a)or ((z+x)>a)):
                    return False
    return True


for i in range(1000):
    if f(i):
        print(i)
