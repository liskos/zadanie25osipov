def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((2*y+3*x)!=23) or ((2*x+3)<a)or ((y*3+11)<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break