def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((x)<50) or ((4*y-3*x)<=144)or (((x-25)**2+(y-25)**2)>a*a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break