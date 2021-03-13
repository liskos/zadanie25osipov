def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((3*y-4*x-29)!=0) or ((x*2*x+5)>a)or ((y*y-1)>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
