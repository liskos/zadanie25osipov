def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((5*y+3*x)!=110) or (x >a)or (2*y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
