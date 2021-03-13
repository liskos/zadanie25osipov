def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                if not(((y+2*x+z)!=48) or (x >a)or (y>a)or (z>a)):
                    return False
    return True


for i in range(1000):
    if f(i):
        print(i)
