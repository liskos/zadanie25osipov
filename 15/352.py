def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((5*y+2*x)!=65) or ((2*x)>a) or ((3*y)>a)):
                return False
    return True


for i in range(1000, -1000, -1):
    if f(i):
        print(i)
        break
