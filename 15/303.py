def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((3*y-x)>a) or ((2*x + 3*y)<30)or ((2*y - x) < -31)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
