def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                if not(((4*y+x*x+3*z)!=156) or (8*x*x >a)or (y>a)or (4*z>a)):
                    return False
    return True


for i in range(1000):
    if f(i):
        print(i)
