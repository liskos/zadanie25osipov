def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y-2*x+29)!=0) or (x >a)or (3*y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
