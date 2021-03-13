def f(a):
    for x in range(300):
        for y in range(150):
            for z in range(300):
                if not(((y+2*x+z)!=220) or (6*x >a)or (y>a)or (2*z>a)):
                    return False
    return True


for i in range(1000,0,-1):
    if f(i):
        print(i)
