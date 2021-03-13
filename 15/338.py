def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((3*y+x)!=22) or ((x*5-8)<a)and ((y*2+3)<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break