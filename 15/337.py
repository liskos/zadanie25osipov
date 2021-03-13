def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((2*y+x)!=17) or ((x*7)<a)and ((y*3)<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break