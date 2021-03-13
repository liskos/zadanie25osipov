def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((21*y-5*x)!=-99) or ((x*2-7)>a)or ((y*y+16)>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
