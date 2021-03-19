def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y-20)<a)and((10-x)<a)or(x*(y+2)>48)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
