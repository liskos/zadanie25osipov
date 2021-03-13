def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((4*y+6*x)!=34) or ((x*5+3*y)<a)and ((y*4+15*x-35)<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break