def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y-x)!=10) or (x >a)or (y>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)