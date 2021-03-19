def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y<=a)or(y<=2*x+4))==(y<=4+abs(x+8)+abs(x-8))):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
