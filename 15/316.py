def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((x)>=13) or (x <3*y)or (y*x<a)):
                return False
    return True


for i in range(1000):
    if f(i):
        print(i)
        break
