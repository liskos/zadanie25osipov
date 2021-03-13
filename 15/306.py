def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y+4*x)!=120) or (x >a)or (y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
