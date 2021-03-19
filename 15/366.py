def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x>4)or((x+2)<y)or((x*x+y*y)<a)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
