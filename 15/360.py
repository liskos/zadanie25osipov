def f(a, b):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y<=-4*x+b)or(y<=2*x*x-12*x+a))==(y<=2+(x-4)**2+abs((x-2)**2-16))):
                return False
    return True


for i in range(10000):
    for i2 in range(10000):
        if f(i, i2):
            print(i, i2)
