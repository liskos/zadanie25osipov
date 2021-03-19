def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x*x-10*x+16)>0)or((y*y-10*y+21)>0)or((x*y)<2*a)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
