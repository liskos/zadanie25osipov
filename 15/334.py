def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((17*y-13*x)!=480) or (((x+5)**2)>a)or ((y*19)>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
