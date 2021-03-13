def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((2*y-x)<a) or (x + 2*y>50)or (2*x + y < 40)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break