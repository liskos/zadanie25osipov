def f(a):
    for x in range(1, 200):
        for y in range(1, 100):
            if not(((4*y-x)>a) or ((x + 6*y)<210)or ((3*y - 2*x) < 30)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
