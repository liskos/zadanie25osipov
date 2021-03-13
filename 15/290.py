def f(a):
    for x in range( 81):
        for y in range( 41):
            if not(((2*y+4*x)<a) or ((x+2*y)>80)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break