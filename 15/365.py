def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x>7)or(y>4)or((x*x+3*y)<a)):
                return False
    return True


for i in range(10000):
    if f(i):
        print(i)
        break
