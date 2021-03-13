def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((x)>40) or ((5*y-3*x)>150)or (((x-20)**2+(y-20)**2)<=a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break