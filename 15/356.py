def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y>=-4*x+12)and(y>=4*x-12))==(y>=a*abs(x-3))):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
