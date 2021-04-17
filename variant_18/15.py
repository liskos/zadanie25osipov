def f(a):
    for x in range(1000):
        for y in range(1000):
            if (x*y>a) and (x>y) and (x<8):
                return False
    return True


for i in range(-10000, 10001):
    if f(i):
        print(i)
        break
