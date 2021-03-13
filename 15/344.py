def f(a):
    for x in range(0, 100):
        for y in range(0, 100):
            if not(((3*y+5*x)!=60) or (x<a and y<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break