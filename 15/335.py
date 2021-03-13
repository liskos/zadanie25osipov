def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((y-x*x)!=-80) or ((x*13-14)>a)or ((y*y+15)>a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
