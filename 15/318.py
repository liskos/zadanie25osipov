def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((2*y+5*x)!=51) or (x >a)or (3*y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
