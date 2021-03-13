def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y+5*x)!=80) or (3*x >a)or (y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
