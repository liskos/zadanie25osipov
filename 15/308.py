def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y+3*x)!=60) or (2*x >a)or (y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
