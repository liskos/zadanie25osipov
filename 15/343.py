def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((x)<50) and ((4*y-3*x)<=144)and (((x-25)**2+(y-25)**2)>(a*a)):
                return False
    return True


for i in range(1, 1000):
    if f(i):
        print(i)
        break