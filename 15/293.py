def f(a):
    for x in range(1, 50):
        for y in range(1, 34):
            if not(((7*y+x)<a) or ((2*x+3*y)>98)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break