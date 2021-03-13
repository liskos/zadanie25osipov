def f(a):
    for x in range(1, 41):
        for y in range(1, 41):
            if not(((2*y+3*x)<a) or ((x+y)>40)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break