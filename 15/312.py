def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((3*y+2*x)!=130) or (3*x >a)or (2*y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
