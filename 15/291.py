def f(a):
    for x in range(1, 28):
        for y in range(1, 42):
            if not(((y+5*x)<a) or ((3*x+2*y)>81)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break